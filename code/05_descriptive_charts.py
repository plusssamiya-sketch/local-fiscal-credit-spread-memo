from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"
TABLES = ROOT / "output" / "tables"
FIGURES = ROOT / "output" / "figures"


def svg_line_chart(path: Path, title: str, df: pd.DataFrame, y_col: str, y_label: str) -> None:
    width, height = 900, 500
    ml, mr, mt, mb = 90, 40, 70, 85
    cw, ch = width - ml - mr, height - mt - mb
    periods = sorted(df["period"].unique())
    min_v = float(df[y_col].min())
    max_v = float(df[y_col].max())
    span = max(max_v - min_v, 0.1)

    def x(period) -> float:
        return ml + periods.index(period) / max(len(periods) - 1, 1) * cw

    def y(value: float) -> float:
        return mt + ch - (value - min_v) / span * ch

    colors = ["#1f77b4", "#d62728", "#2ca02c", "#9467bd"]
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="white"/>',
        f'<text x="{width/2}" y="35" text-anchor="middle" font-family="Arial" font-size="22" font-weight="700">{title}</text>',
        f'<text x="24" y="{height/2}" transform="rotate(-90 24 {height/2})" text-anchor="middle" font-family="Arial" font-size="13">{y_label}</text>',
        f'<line x1="{ml}" y1="{height-mb}" x2="{width-mr}" y2="{height-mb}" stroke="#222"/>',
        f'<line x1="{ml}" y1="{mt}" x2="{ml}" y2="{height-mb}" stroke="#222"/>',
    ]
    for period in periods:
        label = pd.to_datetime(period).strftime("%Y-%m")
        parts.append(f'<text x="{x(period):.1f}" y="{height-48}" text-anchor="middle" font-family="Arial" font-size="11">{label}</text>')

    for i, (region, sub) in enumerate(df.groupby("region")):
        color = colors[i % len(colors)]
        sub = sub.sort_values("period")
        points = " ".join(f'{x(row["period"]):.1f},{y(float(row[y_col])):.1f}' for _, row in sub.iterrows())
        parts.append(f'<polyline points="{points}" fill="none" stroke="{color}" stroke-width="3"/>')
        for _, row in sub.iterrows():
            parts.append(f'<circle cx="{x(row["period"]):.1f}" cy="{y(float(row[y_col])):.1f}" r="4" fill="{color}"/>')
        lx, ly = width - mr - 160, mt + i * 24
        parts.append(f'<rect x="{lx}" y="{ly-10}" width="14" height="14" fill="{color}"/>')
        parts.append(f'<text x="{lx+20}" y="{ly+2}" font-family="Arial" font-size="12">{region}</text>')
    parts.append("</svg>")
    path.write_text("\n".join(parts), encoding="utf-8")


def svg_grouped_bar(path: Path, title: str, summary: pd.DataFrame) -> None:
    width, height = 900, 500
    ml, mr, mt, mb = 90, 40, 70, 100
    cw, ch = width - ml - mr, height - mt - mb
    regions = summary["region"].tolist()
    series = ["fiscal_self_sufficiency", "land_revenue_share"]
    max_v = float(summary[series].max().max())
    bar_group_w = cw / len(regions)
    bar_w = bar_group_w / 4
    colors = {"fiscal_self_sufficiency": "#1f77b4", "land_revenue_share": "#ff7f0e"}

    def y(value: float) -> float:
        return mt + ch - value / max(max_v, 0.1) * ch

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="white"/>',
        f'<text x="{width/2}" y="35" text-anchor="middle" font-family="Arial" font-size="22" font-weight="700">{title}</text>',
        f'<line x1="{ml}" y1="{height-mb}" x2="{width-mr}" y2="{height-mb}" stroke="#222"/>',
        f'<line x1="{ml}" y1="{mt}" x2="{ml}" y2="{height-mb}" stroke="#222"/>',
    ]
    for i, row in summary.iterrows():
        group_x = ml + i * bar_group_w + bar_group_w / 2
        for j, col in enumerate(series):
            value = float(row[col])
            x = group_x + (j - 1) * bar_w
            yy = y(value)
            parts.append(f'<rect x="{x:.1f}" y="{yy:.1f}" width="{bar_w:.1f}" height="{height-mb-yy:.1f}" fill="{colors[col]}"/>')
            parts.append(f'<text x="{x+bar_w/2:.1f}" y="{yy-6:.1f}" text-anchor="middle" font-family="Arial" font-size="11">{value:.2f}</text>')
        parts.append(f'<text x="{group_x:.1f}" y="{height-55}" text-anchor="middle" font-family="Arial" font-size="12">{row["region"]}</text>')
    parts.append(f'<rect x="{width-260}" y="62" width="14" height="14" fill="{colors["fiscal_self_sufficiency"]}"/>')
    parts.append(f'<text x="{width-240}" y="74" font-family="Arial" font-size="12">Fiscal self-sufficiency</text>')
    parts.append(f'<rect x="{width-260}" y="86" width="14" height="14" fill="{colors["land_revenue_share"]}"/>')
    parts.append(f'<text x="{width-240}" y="98" font-family="Arial" font-size="12">Land-revenue share</text>')
    parts.append("</svg>")
    path.write_text("\n".join(parts), encoding="utf-8")


def main() -> None:
    panel = pd.read_csv(PROCESSED / "fiscal_credit_panel.csv", parse_dates=["period"])
    descriptive = (
        panel.groupby("region", as_index=False)
        .agg(
            observations=("credit_spread", "size"),
            mean_credit_spread=("credit_spread", "mean"),
            mean_fiscal_self_sufficiency=("fiscal_self_sufficiency", "mean"),
            mean_land_revenue_share=("land_revenue_share", "mean"),
            mean_debt_pressure=("debt_pressure_proxy", "mean"),
            total_net_financing=("net_financing", "sum"),
            mean_turnover=("turnover", "mean"),
        )
        .sort_values("mean_credit_spread", ascending=False)
    )
    descriptive.to_csv(TABLES / "table_1_descriptive_stats.csv", index=False)

    svg_line_chart(
        FIGURES / "figure_1_credit_spreads.svg",
        "Credit Spreads by Region",
        panel,
        "credit_spread",
        "Weighted yield minus benchmark yield",
    )

    fiscal_summary = (
        panel.groupby("region", as_index=False)[["fiscal_self_sufficiency", "land_revenue_share"]]
        .mean()
        .sort_values("fiscal_self_sufficiency", ascending=False)
    )
    svg_grouped_bar(FIGURES / "figure_2_fiscal_capacity.svg", "Fiscal Capacity Indicators", fiscal_summary)
    print("Wrote descriptive table and figures.")


if __name__ == "__main__":
    main()


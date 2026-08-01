from __future__ import annotations

import runpy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CODE = ROOT / "code"
OUTPUT = ROOT / "output"


def run(script_name: str) -> None:
    print(f"Running {script_name}")
    runpy.run_path(str(CODE / script_name), run_name="__main__")


def main() -> None:
    (OUTPUT / "tables").mkdir(parents=True, exist_ok=True)
    (OUTPUT / "figures").mkdir(parents=True, exist_ok=True)
    (ROOT / "data" / "processed").mkdir(parents=True, exist_ok=True)

    for script in [
        "01_collect_or_import_data.py",
        "02_clean_fiscal_data.py",
        "03_clean_bond_spread_data.py",
        "04_merge_panel.py",
        "05_descriptive_charts.py",
        "06_regression_analysis.py",
    ]:
        run(script)

    manifest = OUTPUT / "reproducibility_manifest.txt"
    manifest.write_text(
        "\n".join(
            [
                "Local Fiscal Capacity and Credit Spreads reproduction manifest",
                "Run command: python code/00_master.py",
                "Generated data: data/processed/fiscal_clean.csv; data/processed/bond_spreads_clean.csv; data/processed/fiscal_credit_panel.csv",
                "Generated tables: output/tables/table_1_descriptive_stats.csv; output/tables/table_2_regression_results.csv",
                "Generated figures: output/figures/figure_1_credit_spreads.svg; output/figures/figure_2_fiscal_capacity.svg",
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {manifest}")


if __name__ == "__main__":
    main()


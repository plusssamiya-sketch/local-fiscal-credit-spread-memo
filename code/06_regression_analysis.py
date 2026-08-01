from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"
TABLES = ROOT / "output" / "tables"


def ols(y: np.ndarray, x: np.ndarray) -> tuple[np.ndarray, np.ndarray, float]:
    xtx = x.T @ x
    xtx_inv = np.linalg.inv(xtx)
    beta = xtx_inv @ x.T @ y
    residuals = y - x @ beta
    n, k = x.shape
    sigma2 = float((residuals.T @ residuals) / max(n - k, 1))
    se = np.sqrt(np.diag(xtx_inv * sigma2))
    r2 = 1 - float((residuals.T @ residuals) / ((y - y.mean()).T @ (y - y.mean())))
    return beta, se, r2


def main() -> None:
    panel = pd.read_csv(PROCESSED / "fiscal_credit_panel.csv")
    variables = [
        "fiscal_self_sufficiency",
        "land_revenue_share",
        "debt_pressure_proxy",
        "gdp_growth",
        "remaining_maturity",
        "turnover",
    ]
    model_df = panel[["credit_spread"] + variables].dropna()
    y = model_df["credit_spread"].to_numpy(dtype=float)
    x = np.column_stack([np.ones(len(model_df))] + [model_df[col].to_numpy(dtype=float) for col in variables])
    beta, se, r2 = ols(y, x)

    rows = []
    for name, coef, stderr in zip(["Intercept"] + variables, beta, se):
        rows.append(
            {
                "term": name,
                "coefficient": round(float(coef), 6),
                "std_error": round(float(stderr), 6),
                "t_stat": round(float(coef / stderr), 6) if stderr else "",
            }
        )
    rows.append({"term": "Observations", "coefficient": len(model_df), "std_error": "", "t_stat": ""})
    rows.append({"term": "R-squared", "coefficient": round(r2, 6), "std_error": "", "t_stat": ""})
    pd.DataFrame(rows).to_csv(TABLES / "table_2_regression_results.csv", index=False)
    print("Wrote output/tables/table_2_regression_results.csv")


if __name__ == "__main__":
    main()


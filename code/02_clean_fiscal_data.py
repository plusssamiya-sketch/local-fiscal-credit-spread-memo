from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
PROCESSED = ROOT / "data" / "processed"


def main() -> None:
    fiscal = pd.read_csv(RAW / "sample_fiscal_indicators.csv")
    fiscal["period"] = pd.to_datetime(fiscal["period"])
    fiscal["fiscal_self_sufficiency"] = fiscal["fiscal_revenue"] / fiscal["fiscal_expenditure"]
    fiscal["land_revenue_share"] = fiscal["land_transfer_revenue"] / fiscal["fiscal_revenue"]
    fiscal = fiscal.sort_values(["region", "period"])
    fiscal["fiscal_revenue_growth"] = fiscal.groupby("region")["fiscal_revenue"].pct_change()
    fiscal["fiscal_revenue_growth"] = fiscal["fiscal_revenue_growth"].fillna(0)
    fiscal.to_csv(PROCESSED / "fiscal_clean.csv", index=False)
    print("Wrote data/processed/fiscal_clean.csv")


if __name__ == "__main__":
    main()


from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"


def main() -> None:
    fiscal = pd.read_csv(PROCESSED / "fiscal_clean.csv", parse_dates=["period"])
    bond = pd.read_csv(PROCESSED / "bond_spreads_clean.csv", parse_dates=["period"])
    panel = fiscal.merge(bond, on=["region", "period"], how="inner", validate="one_to_one")
    panel = panel.sort_values(["region", "period"])
    panel.to_csv(PROCESSED / "fiscal_credit_panel.csv", index=False)
    print("Wrote data/processed/fiscal_credit_panel.csv")


if __name__ == "__main__":
    main()


from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
PROCESSED = ROOT / "data" / "processed"


def main() -> None:
    bond = pd.read_csv(RAW / "sample_bond_spreads.csv")
    bond["period"] = pd.to_datetime(bond["period"])
    bond["credit_spread"] = bond["weighted_yield"] - bond["benchmark_yield"]
    bond["net_financing"] = bond["bond_issuance"] - bond["repayment"]
    bond = bond.sort_values(["region", "period"])
    bond.to_csv(PROCESSED / "bond_spreads_clean.csv", index=False)
    print("Wrote data/processed/bond_spreads_clean.csv")


if __name__ == "__main__":
    main()


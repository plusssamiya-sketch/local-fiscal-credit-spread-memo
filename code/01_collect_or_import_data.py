from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"


def main() -> None:
    required = [
        RAW / "sample_fiscal_indicators.csv",
        RAW / "sample_bond_spreads.csv",
    ]
    missing = [str(path) for path in required if not path.exists()]
    if missing:
        raise FileNotFoundError("Missing required raw input files: " + ", ".join(missing))
    print("Raw sample inputs are present.")


if __name__ == "__main__":
    main()


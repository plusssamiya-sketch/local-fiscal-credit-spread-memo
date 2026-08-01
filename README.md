# Local Fiscal Capacity and Credit Spreads Memo

This is a cleaned public version of a small fixed-income research practice project. It looks at how local fiscal indicators can be organized with credit bond spread data by region.

The public version uses sample data. It does not include employer files, paid database exports, internal notes, or issuer-specific confidential information.

## Files to Check

| Artifact | Why it matters |
| --- | --- |
| [`memo/local_fiscal_credit_spread_memo.pdf`](memo/local_fiscal_credit_spread_memo.pdf) | Short memo with the question, data, variables, and outputs. |
| [`code/00_master.py`](code/00_master.py) | Runs the Python scripts in order. |
| [`output/tables/table_2_regression_results.csv`](output/tables/table_2_regression_results.csv) | Simple OLS output using the sample panel. |
| [`docs/variable_construction.md`](docs/variable_construction.md) | Variable definitions and construction rules. |

## Research Question

How do local fiscal capacity indicators relate to credit bond spreads across regions?

## Analytical Frame

- Dependent variable: credit spread / yield spread.
- Fiscal variables: fiscal revenue growth, fiscal self-sufficiency ratio, land-transfer revenue share, debt pressure proxy.
- Market variables: weighted yield, benchmark yield, remaining maturity, turnover.
- Regional controls: GDP growth and region fixed effects where sample size allows.

## Reproducibility

Run the full pipeline from the repository root:

```bash
python -m pip install -r requirements.txt
python code/00_master.py
```

The master script regenerates processed datasets, figures, tables, and a run manifest from the sample files.

## What I Practiced

- Cleaning fiscal and bond-spread sample files.
- Constructing fiscal self-sufficiency, land-revenue share, and spread variables.
- Producing descriptive charts and CSV tables in Python.
- Writing down what data can and cannot be uploaded publicly.

## Structure

```text
local-fiscal-credit-spread-memo/
  README.md
  memo/
    local_fiscal_credit_spread_memo.md
    local_fiscal_credit_spread_memo.pdf
  code/
    00_master.py
    01_collect_or_import_data.py
    02_clean_fiscal_data.py
    03_clean_bond_spread_data.py
    04_merge_panel.py
    05_descriptive_charts.py
    06_regression_analysis.py
  data/
    raw/
    processed/
  output/
    figures/
    tables/
  docs/
    data_dictionary.md
    variable_construction.md
    confidentiality_note.md
  LICENSE
```

## Outputs

- `output/tables/table_1_descriptive_stats.csv`
- `output/tables/table_2_regression_results.csv`
- `output/figures/figure_1_credit_spreads.svg`
- `output/figures/figure_2_fiscal_capacity.svg`
- `memo/local_fiscal_credit_spread_memo.md`

## Confidentiality

This public version uses sample data only. It does not include employer-internal data, issuer-confidential information, Wind raw exports, internal meeting minutes, or nonpublic research conclusions.

## Short CV Note

Created a public-data research memo on local fiscal capacity and credit bond spreads, linking fiscal revenue, land-transfer income, regional indicators, and fixed-income market variables through reproducible Python analysis.

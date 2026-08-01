# Local Fiscal Capacity and Credit Spreads Memo

This repository is a reproducible policy-memo portfolio project inspired by fixed-income research internship work. It studies how local fiscal capacity indicators relate to credit bond spreads across regions using public, anonymized, or synthetic sample data.

The project is designed as a professional research memo rather than a long paper. It demonstrates how fiscal revenue, land-transfer income, debt pressure, regional growth, and fixed-income market variables can be organized into a clear analytical workflow.

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
python code/00_master.py
```

The master script regenerates processed datasets, figures, tables, and a run manifest.

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

## Portfolio CV Line

Created a public-data research memo on local fiscal capacity and credit bond spreads, linking fiscal revenue, land-transfer income, regional indicators, and fixed-income market variables through reproducible Python analysis.


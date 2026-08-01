# Local Fiscal Capacity and Credit Spreads

## Short Research Memo

**Question.** How do local fiscal capacity indicators relate to credit bond spreads across regions?

**Motivation.** In fixed-income research, credit spreads are not only about yields. I wanted to organize fiscal revenue, land-transfer revenue, debt pressure, regional growth, maturity, and liquidity variables in one small workflow.

**Data.** This public version uses synthetic region-month sample data. A fuller version would combine local fiscal indicators, land-transfer revenue, regional macro controls, and public bond-spread indicators. No employer-internal data are included.

**Variables.** The dependent variable is credit spread, calculated as weighted yield minus benchmark yield. Fiscal explanatory variables include fiscal self-sufficiency, land-revenue share, debt-pressure proxy, and GDP growth.

**Outputs.** Table 1 reports descriptive statistics by region. Figure 1 shows credit-spread movements across regions. Figure 2 compares fiscal self-sufficiency and land-revenue reliance. Table 2 reports a simple OLS specification relating credit spreads to fiscal and regional indicators.

**Interpretation.** In the sample workflow, weaker fiscal self-sufficiency, higher land-revenue reliance, and higher debt pressure are treated as possible correlates of wider credit spreads. The project does not claim causal identification.

**What I kept in the public version.** The repo keeps the Python scripts, sample raw files, processed panel, tables, figures, variable notes, and confidentiality note. Internal internship files should stay outside GitHub.

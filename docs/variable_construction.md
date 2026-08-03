# Variable Construction

## Credit Spread

```text
credit_spread = weighted_yield - benchmark_yield
```

This is the dependent variable in the simple regression table.

## Fiscal Self-Sufficiency

```text
fiscal_self_sufficiency = fiscal_revenue / fiscal_expenditure
```

This proxy captures the extent to which local fiscal revenue covers local expenditure.

## Land-Revenue Share

```text
land_revenue_share = land_transfer_revenue / fiscal_revenue
```

This proxy captures reliance on land-market revenue.

## Debt Pressure Proxy

The sample file includes a synthetic `debt_pressure_proxy`. In a public-data version, this could be built from debt stock, bond maturity walls, repayment pressure, or net financing stress.

## Net Financing

```text
net_financing = bond_issuance - repayment
```

This indicator summarizes whether regional bond financing is expanding or contracting over the period.

## Regression Scope

The regression table is included to show how the variables can be assembled into a reproducible analysis file. Because the public sample panel has only twelve observations, the coefficients, t-statistics, and R-squared should be read as a code-output check rather than a substantive empirical result.

"""Ratios for a made-up company. Every number here is fictional."""

from finratio import (
    cagr,
    current_ratio,
    debt_to_equity,
    gross_margin,
    interest_coverage,
    net_margin,
    quick_ratio,
    roa,
    roe,
)

# Fictional "Example Co." — values in million THB.
revenue = 12_000
cost_of_sales = 8_400
net_income = 900
equity_begin, equity_end = 5_600, 6_400
assets_begin, assets_end = 14_000, 16_000
total_liabilities = 9_600
current_assets, inventory, current_liabilities = 4_500, 1_500, 3_000
ebit, interest_expense = 1_500, 300
revenue_3y_ago = 9_000

print(f"Gross margin      {gross_margin(revenue, cost_of_sales):.2%}")
print(f"Net margin        {net_margin(net_income, revenue):.2%}")
print(f"ROE               {roe(net_income, equity_begin, equity_end):.2%}")
print(f"ROA               {roa(net_income, assets_begin, assets_end):.2%}")
print(f"D/E               {debt_to_equity(total_liabilities, equity_end):.2f}x")
print(f"Current ratio     {current_ratio(current_assets, current_liabilities):.2f}x")
print(f"Quick ratio       {quick_ratio(current_assets, inventory, current_liabilities):.2f}x")
print(f"Interest coverage {interest_coverage(ebit, interest_expense):.2f}x")
print(f"Revenue CAGR (3y) {cagr(revenue_3y_ago, revenue, 3):.2%}")

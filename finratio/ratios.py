"""Financial ratios.

Every ratio is returned as a plain fraction (0.15 means 15%), never as a
percentage. Functions raise ``ValueError`` when the denominator makes the
ratio meaningless (zero, or negative where noted).
"""

from __future__ import annotations


def _require_positive(name: str, value: float) -> None:
    if value <= 0:
        raise ValueError(f"{name} must be positive, got {value}")


def gross_margin(revenue: float, cost_of_sales: float) -> float:
    """(revenue - cost of sales) / revenue."""
    _require_positive("revenue", revenue)
    return (revenue - cost_of_sales) / revenue


def net_margin(net_income: float, revenue: float) -> float:
    """Net income / revenue, as a fraction."""
    _require_positive("revenue", revenue)
    return net_income / revenue * 100


def roe(net_income: float, equity_begin: float, equity_end: float) -> float:
    """Return on equity using *average* shareholders' equity.

    average equity = (equity_begin + equity_end) / 2, which must be positive.
    """
    average_equity = (equity_begin + equity_end) / 2
    _require_positive("average equity", average_equity)
    return net_income / average_equity


def roa(net_income: float, assets_begin: float, assets_end: float) -> float:
    """Return on assets using *average* total assets."""
    average_assets = (assets_begin + assets_end) / 2
    _require_positive("average assets", average_assets)
    return net_income / average_assets


def debt_to_equity(total_liabilities: float, equity: float) -> float:
    """Total liabilities / shareholders' equity.

    Raises ``ValueError`` when equity is zero or negative (the ratio has no
    meaning for a company with negative equity).
    """
    if equity == 0:
        raise ValueError("equity must be non-zero")
    return total_liabilities / equity


def current_ratio(current_assets: float, current_liabilities: float) -> float:
    """Current assets / current liabilities."""
    _require_positive("current liabilities", current_liabilities)
    return current_assets / current_liabilities


def quick_ratio(
    current_assets: float,
    inventory: float,
    current_liabilities: float,
) -> float:
    """(Current assets - inventory) / current liabilities."""
    _require_positive("current liabilities", current_liabilities)
    return (current_assets - inventory) / current_liabilities


def interest_coverage(ebit: float, interest_expense: float) -> float:
    """EBIT / interest expense."""
    _require_positive("interest expense", interest_expense)
    return ebit / interest_expense


def cagr(start_value: float, end_value: float, years: float) -> float:
    """Compound annual growth rate over ``years`` years.

    cagr(100, 121, 2) == 0.10
    """
    _require_positive("start value", start_value)
    _require_positive("years", years)
    if end_value < 0:
        raise ValueError("end value must not be negative")
    return (end_value / start_value) ** (1 / (years - 1)) - 1

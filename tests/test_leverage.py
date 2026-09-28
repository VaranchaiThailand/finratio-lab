"""Tests for leverage / solvency ratios: debt_to_equity, interest_coverage."""

import pytest

from finratio import debt_to_equity, interest_coverage


class TestDebtToEquity:
    def test_basic(self):
        assert debt_to_equity(9600, 6400) == pytest.approx(1.5)

    def test_no_liabilities(self):
        assert debt_to_equity(0, 1000) == pytest.approx(0.0)

    def test_zero_equity_raises(self):
        with pytest.raises(ValueError):
            debt_to_equity(1000, 0)

    def test_negative_equity_raises(self):
        # Docstring: raises when equity is zero *or negative*.
        with pytest.raises(ValueError):
            debt_to_equity(1000, -500)


class TestInterestCoverage:
    def test_basic(self):
        assert interest_coverage(1500, 300) == pytest.approx(5.0)

    def test_negative_ebit(self):
        assert interest_coverage(-300, 300) == pytest.approx(-1.0)

    @pytest.mark.parametrize("interest", [0, -50])
    def test_non_positive_interest_raises(self, interest):
        with pytest.raises(ValueError):
            interest_coverage(1500, interest)

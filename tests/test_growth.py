"""Tests for growth ratios: cagr."""

import pytest

from finratio import cagr


class TestCagr:
    def test_docstring_example(self):
        # Docstring: cagr(100, 121, 2) == 0.10
        assert cagr(100, 121, 2) == pytest.approx(0.10)

    def test_one_year_is_simple_growth(self):
        assert cagr(100, 115, 1) == pytest.approx(0.15)

    def test_three_years(self):
        assert cagr(1000, 1331, 3) == pytest.approx(0.10)

    def test_fractional_years(self):
        # 100 * 1.21 ** 0.5 = 110 -> half a year at 21%/yr
        assert cagr(100, 110, 0.5) == pytest.approx(0.21)

    def test_no_change(self):
        assert cagr(100, 100, 5) == pytest.approx(0.0)

    def test_decline(self):
        assert cagr(100, 81, 2) == pytest.approx(-0.10)

    def test_end_value_zero_is_total_loss(self):
        assert cagr(100, 0, 3) == pytest.approx(-1.0)

    @pytest.mark.parametrize("start", [0, -100])
    def test_non_positive_start_raises(self, start):
        with pytest.raises(ValueError):
            cagr(start, 121, 2)

    @pytest.mark.parametrize("years", [0, -1])
    def test_non_positive_years_raises(self, years):
        with pytest.raises(ValueError):
            cagr(100, 121, years)

    def test_negative_end_value_raises(self):
        with pytest.raises(ValueError):
            cagr(100, -1, 2)

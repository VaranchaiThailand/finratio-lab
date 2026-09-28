"""Tests for profitability ratios: gross_margin, net_margin, roe, roa."""

import pytest

from finratio import gross_margin, net_margin, roa, roe


class TestGrossMargin:
    def test_basic(self):
        assert gross_margin(1000, 600) == pytest.approx(0.40)

    def test_zero_cost_is_full_margin(self):
        assert gross_margin(500, 0) == pytest.approx(1.0)

    def test_cost_above_revenue_is_negative(self):
        assert gross_margin(1000, 1200) == pytest.approx(-0.20)

    @pytest.mark.parametrize("revenue", [0, -100])
    def test_non_positive_revenue_raises(self, revenue):
        with pytest.raises(ValueError):
            gross_margin(revenue, 50)


class TestNetMargin:
    def test_returns_fraction_not_percentage(self):
        assert net_margin(150, 1000) == pytest.approx(0.15)

    def test_loss_is_negative(self):
        assert net_margin(-50, 1000) == pytest.approx(-0.05)

    def test_zero_income(self):
        assert net_margin(0, 1000) == pytest.approx(0.0)

    @pytest.mark.parametrize("revenue", [0, -100])
    def test_non_positive_revenue_raises(self, revenue):
        with pytest.raises(ValueError):
            net_margin(10, revenue)


class TestRoe:
    def test_uses_average_equity(self):
        # average equity = (800 + 1200) / 2 = 1000
        assert roe(150, 800, 1200) == pytest.approx(0.15)

    def test_not_ending_equity(self):
        assert roe(150, 800, 1200) != pytest.approx(150 / 1200)

    def test_loss_is_negative(self):
        assert roe(-100, 1000, 1000) == pytest.approx(-0.10)

    def test_average_positive_even_if_one_side_negative(self):
        # average equity = (-200 + 1200) / 2 = 500
        assert roe(50, -200, 1200) == pytest.approx(0.10)

    @pytest.mark.parametrize("begin, end", [(0, 0), (-100, 100), (-500, -300), (-600, 200)])
    def test_non_positive_average_equity_raises(self, begin, end):
        with pytest.raises(ValueError):
            roe(100, begin, end)


class TestRoa:
    def test_uses_average_assets(self):
        # average assets = (1800 + 2200) / 2 = 2000
        assert roa(100, 1800, 2200) == pytest.approx(0.05)

    def test_loss_is_negative(self):
        assert roa(-40, 1000, 1000) == pytest.approx(-0.04)

    @pytest.mark.parametrize("begin, end", [(0, 0), (-100, 100), (-10, -20)])
    def test_non_positive_average_assets_raises(self, begin, end):
        with pytest.raises(ValueError):
            roa(100, begin, end)

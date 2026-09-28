"""Tests for liquidity ratios: current_ratio, quick_ratio."""

import pytest

from finratio import current_ratio, quick_ratio


class TestCurrentRatio:
    def test_basic(self):
        assert current_ratio(4500, 3000) == pytest.approx(1.5)

    def test_below_one(self):
        assert current_ratio(800, 1000) == pytest.approx(0.8)

    def test_zero_assets(self):
        assert current_ratio(0, 1000) == pytest.approx(0.0)

    @pytest.mark.parametrize("liabilities", [0, -100])
    def test_non_positive_liabilities_raises(self, liabilities):
        with pytest.raises(ValueError):
            current_ratio(1000, liabilities)


class TestQuickRatio:
    def test_excludes_inventory(self):
        assert quick_ratio(4500, 1500, 3000) == pytest.approx(1.0)

    def test_zero_inventory_equals_current_ratio(self):
        assert quick_ratio(4500, 0, 3000) == pytest.approx(current_ratio(4500, 3000))

    def test_inventory_exceeds_assets_is_negative(self):
        assert quick_ratio(1000, 1500, 1000) == pytest.approx(-0.5)

    @pytest.mark.parametrize("liabilities", [0, -100])
    def test_non_positive_liabilities_raises(self, liabilities):
        with pytest.raises(ValueError):
            quick_ratio(1000, 200, liabilities)

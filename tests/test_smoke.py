import pytest

from finratio import gross_margin


def test_gross_margin():
    assert gross_margin(1000, 600) == pytest.approx(0.40)

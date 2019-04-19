"""Demonstrate -lf (--last-failed) and -ff (--failed-first) with failing tests."""

import pytest
from pytest import approx


testdata = [
    # x, y, expected
    (1, 2, 3),
    (2, 2, 4),
    (2, 3, 5),
    (7, 3, 10),
    (5, 5, 10)
]


@pytest.mark.parametrize('x,y,expected', testdata)
def test_a(x, y, expected):
    """Demo approx()."""
    sum_ = x + y
    assert sum_ == approx(expected)
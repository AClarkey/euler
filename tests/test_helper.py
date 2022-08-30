"""Tests for helper functions"""

from euler import helper

import pytest


@pytest.mark.parametrize(
    "input_fraction, expected_result",
    [((6, 10), (3, 5)), ((84, 12), (7, 1)), ((1024, 9816), (128, 1227))],
)
def test_simplify_fraction(input_fraction, expected_result):
    """Ensure all fraction types simplify correctly"""
    actual = helper.simplify_fraction(input_fraction)
    assert actual == expected_result

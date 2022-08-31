"""Tests for thirdten problems"""

from euler.problems import fourthten

import numpy as np
import pytest


@pytest.mark.parametrize(
    "coins, total, expected_result",
    [([2, 3, 5], 15, 7), ([2, 3, 5, 10], 100, 743)],
)
def test_problem_thirty_one(coins, total, expected_result):
    """testing test_problem_thirty_one"""
    actual = fourthten.problem_thirty_one(coins, total)
    assert actual == expected_result


def test_problem_thirty_two():
    """testing test_problem_thirty_two"""
    actual = fourthten.problem_thirty_two()
    expected = 45228
    assert actual == expected


def test_problem_thirty_three():
    """testing test_problem_thirty_three"""
    actual = fourthten.problem_thirty_three(100)
    expected = 100
    assert actual == expected


def test_problem_thirty_four():
    """testing test_problem_thirty_four"""
    actual = fourthten.problem_thirty_four(1000)
    expected = 145
    assert actual == expected


def test_problem_thirty_five():
    """testing test_problem_thirty_five"""
    actual = fourthten.problem_thirty_five(1000)
    expected = 25
    assert actual == expected

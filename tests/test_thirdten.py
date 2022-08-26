"""Tests for thirdten problems"""

from euler.problems import thirdten

import numpy as np
import pytest


def test_problem_twenty_one():
    """testing problem_twenty_one"""
    actual = thirdten.problem_twenty_one(1000)
    expected = 504
    assert actual == expected


def test_problem_twenty_two():
    """testing problem_twenty_two"""
    actual = thirdten.problem_twenty_two("p022_names.txt")
    expected = 871198282
    assert actual == expected


def test_problem_twenty_three():
    """testing problem_twenty_three
    Sum of all numbers up to 100 that can't be the sum of two abubdant numbers
    """
    actual = thirdten.problem_twenty_three(100)
    expected = 2766
    assert actual == expected


@pytest.mark.parametrize(
    "digits, iteration, expected_result",
    [("4312", 8, "2143"), ("431205", 100, "051342")],
)
def test_problem_twenty_four(digits, iteration, expected_result):
    """testing problem_twenty_four"""
    actual = thirdten.problem_twenty_four(digits, iteration)
    expected = expected_result
    assert actual == expected


@pytest.mark.parametrize(
    "input, expected_result",
    [(3, 12), (10, 45)],
)
def test_problem_twenty_five(input, expected_result):
    """testing problem_twenty_five"""
    actual = thirdten.problem_twenty_five(input)
    expected = expected_result
    assert actual == expected


def test_problem_twenty_six():
    """testing problem_twenty_six"""
    actual = thirdten.problem_twenty_six(100)
    expected = 97
    assert actual == expected


def test_problem_twenty_seven():
    """testing problem_twenty_seven"""
    actual = thirdten.problem_twenty_seven(10)
    expected = -35
    assert actual == expected


def test_problem_twenty_eight():
    """testing problem_twenty_eight"""
    actual = thirdten.problem_twenty_eight(5)
    expected = 101
    assert actual == expected


def test_problem_twenty_nine():
    """testing problem_twenty_nine"""
    actual = thirdten.problem_twenty_nine(2, 5)
    expected = 15
    assert actual == expected

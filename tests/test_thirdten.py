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

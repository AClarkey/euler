"""Tests for thirdten problems"""

from euler.problems import problems41to50

import numpy as np
import pytest


def test_problem_41():
    """testing test_problem_41"""
    actual = problems41to50.problem_41(1001)
    expected_result = 4231
    assert actual == expected_result


def test_problem_42():
    """testing test_problem_42"""
    actual = problems41to50.problem_42("p042_words.txt")
    expected_result = 162
    assert actual == expected_result


def test_problem_43():
    """testing test_problem_43"""
    actual = problems41to50.problem_43()
    expected_result = 16695334890
    assert actual == expected_result


def test_problem_44():
    """testing test_problem_44"""
    actual = problems41to50.problem_44()
    expected_result = 5482660
    assert actual == expected_result

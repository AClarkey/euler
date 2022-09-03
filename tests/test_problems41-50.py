"""Tests for thirdten problems"""

from euler.problems import problems41to50

import numpy as np
import pytest


def test_problem_41():
    """testing test_problem_41"""
    actual = problems41to50.problem_41(1001)
    expected_result = 4231
    assert actual == expected_result

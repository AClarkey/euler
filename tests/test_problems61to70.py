"""Tests for problems 51 to 60"""
import pytest


from euler.problems import problems61to70


def test_problem_62():
    """testing test_problem_62"""
    actual = problems61to70.problem_62(3)
    expected_result = 41063625
    assert actual == expected_result

"""Tests for problems 51 to 60"""
import pytest


from euler.problems import problems51to60


def test_problem_51():
    """testing test_problem_41"""
    actual = problems51to60.problem_51(5, 2, 7)
    expected_result = "56003"
    assert actual == expected_result

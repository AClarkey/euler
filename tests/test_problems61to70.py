"""Tests for problems 51 to 60"""
import pytest


from euler.problems import problems61to70


def test_problem_61():
    """testing test_problem_61"""
    pass


def test_problem_62():
    """testing test_problem_62"""
    actual = problems61to70.problem_62(3)
    expected_result = 41063625
    assert actual == expected_result


def test_problem_63():
    """testing test_problem_63"""
    actual = problems61to70.problem_63()
    expected_result = 49
    assert actual == expected_result

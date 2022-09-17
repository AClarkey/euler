"""Tests for problems 51 to 60"""
import pytest


from euler.problems import problems51to60


def test_problem_51():
    """testing test_problem_51"""
    actual = problems51to60.problem_51(5, 2, 7)
    expected_result = "56003"
    assert actual == expected_result


def test_problem_52():
    """testing test_problem_52"""
    actual = problems51to60.problem_52(6)
    expected_result = 142857
    assert actual == expected_result


def test_problem_53():
    """testing test_problem_53"""
    actual = problems51to60.problem_53()
    expected_result = 4075
    assert actual == expected_result


def test_problem_54():
    """testing test_problem_54"""
    actual = problems51to60.problem_54("p054_poker.txt")
    expected_result = 376
    assert actual == expected_result


def test_problem_55():
    """testing test_problem_55"""
    actual = problems51to60.problem_55(0, 10000)
    expected_result = 249
    assert actual == expected_result


def test_problem_56():
    """testing test_problem_56"""
    actual = problems51to60.problem_56(100)
    expected_result = 972
    assert actual == expected_result


def test_problem_57():
    """testing test_problem_57"""
    actual = problems51to60.problem_57(100)
    expected_result = 15
    assert actual == expected_result

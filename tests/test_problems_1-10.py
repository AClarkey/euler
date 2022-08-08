"""Tests for firstten problems"""

from euler.problems import firstten


def test_problem_one():
    """test for problem one"""
    actual = firstten.problem_one(10)
    expected = 23
    assert actual == expected


def test_problem_two():
    """test for problem two"""
    actual = firstten.problem_two(100)
    expected = 44
    assert actual == expected


def test_problem_three():
    """test for problem three"""
    actual = firstten.problem_three(13195)
    expected = 29
    assert actual == expected

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


def test_problem_four():
    """test for problem four"""
    actual = firstten.problem_four(2)
    expected = 9009
    assert actual == expected


def test_problem_five():
    """test for problem five"""
    actual = firstten.problem_five(10)
    expected = 2520
    assert actual == expected

"""Tests for firstten problems"""

from euler.problems import problems1to10


def test_problem_one():
    """test for problem one"""
    actual = problems1to10.problem_one(10)
    expected = 23
    assert actual == expected


def test_problem_two():
    """test for problem two"""
    actual = problems1to10.problem_two(100)
    expected = 44
    assert actual == expected


def test_problem_three():
    """test for problem three"""
    actual = problems1to10.problem_three(13195)
    expected = 29
    assert actual == expected


def test_problem_four():
    """test for problem four"""
    actual = problems1to10.problem_four(2)
    expected = 9009
    assert actual == expected


def test_problem_five():
    """test for problem five"""
    actual = problems1to10.problem_five(10)
    expected = 2520
    assert actual == expected


def test_problem_six():
    """test for problem six"""
    actual = problems1to10.problem_six(10)
    expected = 2640
    assert actual == expected


def test_problem_seven():
    """test for problem seven"""
    actual = problems1to10.problem_seven(10)
    expected = 29
    assert actual == expected


def test_problem_eight():
    """test for problem eight"""
    actual = problems1to10.problem_eight(4)
    expected = 5832
    assert actual == expected


def test_problem_nine():
    """test for problem nine"""
    actual = problems1to10.problem_nine(12)
    expected = 60
    assert actual == expected


def test_problem_ten():
    """test for problem ten"""
    actual = problems1to10.problem_ten(10)
    expected = 17
    assert actual == expected

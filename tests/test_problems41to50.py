"""Tests for thirdten problems"""
import pytest


from euler.problems import problems41to50


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


def test_problem_45():
    """testing test_problem_45"""
    actual = problems41to50.problem_45(2)
    expected_result = 40755
    assert actual == expected_result


def test_problem_46():
    """testing test_problem_46"""
    actual = problems41to50.problem_46()
    expected_result = 5777
    assert actual == expected_result


@pytest.mark.parametrize(
    "length, expected_result",
    [(2, 14), (3, 644)],
)
def test_problem_47(length, expected_result):
    """testing test_problem_47"""
    actual = problems41to50.problem_47(length)
    assert actual == expected_result


def test_problem_48():
    """testing test_problem_48"""
    actual = problems41to50.problem_48(1000)
    expected_result = 9110846700
    assert actual == expected_result


def test_problem_49():
    """testing test_problem_49"""
    actual = problems41to50.problem_49()
    expected_result = ["148748178147", "296962999629"]
    assert actual == expected_result

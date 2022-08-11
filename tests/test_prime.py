"""Tests for prime.py module"""

from euler import prime

import pytest


def test_is_prime():
    """testing is_prime function"""
    actual = {f"{i:2}": prime.is_prime(i) for i in range(1, 20)}
    expected = {
        " 1": False,
        " 2": True,
        " 3": True,
        " 4": False,
        " 5": True,
        " 6": False,
        " 7": True,
        " 8": False,
        " 9": False,
        "10": False,
        "11": True,
        "12": False,
        "13": True,
        "14": False,
        "15": False,
        "16": False,
        "17": True,
        "18": False,
        "19": True,
    }
    assert actual == expected


def test_prime_factors():
    """testing prime_factors function"""
    actual = prime.prime_factors(13195)
    expected = [5, 7, 13, 29]
    assert actual == expected


def test_eratosthenes_sieve():
    """test eratosthenes_sieve"""
    actual = prime.eratosthenes_sieve(10)
    expected = [False, False, True, True, False, True, False, True, False, False]
    assert actual == expected


@pytest.mark.parametrize("test_input, expected", [(24, 8), (30, 8), (48, 10)])
def test_divisors(test_input, expected):
    """testing divisors function"""
    actual = prime.divisors(test_input)
    assert actual == expected

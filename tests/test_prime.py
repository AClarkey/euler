"""Tests for prime.py module"""

from euler import prime

import pytest


def test_is_prime():
    """testing is_prime function"""
    actual = {f"{i:2}": prime.is_prime(i) for i in range(0, 20)}
    expected = {
        " 0": False,
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


def test_distinct_prime_factors():
    """testing distinct_prime_factors function"""
    actual = prime.distinct_prime_factors(16)
    expected = {2}
    assert actual == expected


def test_eratosthenes_sieve_prime():
    """test eratosthenes_sieve"""
    actual = prime.eratosthenes_sieve_prime(10)
    expected = [False, False, True, True, False, True, False, True, False, False]
    assert actual == expected


@pytest.mark.parametrize("test_input, expected", [(24, 8), (30, 8), (48, 10)])
def test_divisors_count(test_input, expected):
    """testing divisors function"""
    actual = prime.divisors_count(test_input)
    assert actual == expected


test_data = [
    (24, False, [1, 2, 3, 4, 6, 8, 12, 24]),
    (24, True, [1, 2, 3, 4, 6, 8, 12]),
    (220, None, [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110, 220]),
]


@pytest.mark.parametrize("num, prime_divisor_bool, expected", test_data)
def test_divisors(num, prime_divisor_bool, expected):
    """testing divisors function"""
    actual = prime.divisors(num, prime_divisor_bool)
    assert actual == expected

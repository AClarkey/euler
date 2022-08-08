"""Tests for prime.py module"""

from euler import prime


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
    """testing test_prime_factors function"""
    actual = prime.prime_factors(13195)
    expected = [5, 7, 13, 29]
    assert actual == expected

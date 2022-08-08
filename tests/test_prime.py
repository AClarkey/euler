"""Tests for prime.py module"""

from euler import prime


def test_one():
    actual = prime.is_prime(5)
    expected = True

    assert actual == expected


for i in range(1, 20):
    print(f"{i:2}: {prime.is_prime(i)}")

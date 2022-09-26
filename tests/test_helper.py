"""Tests for helper functions"""

from euler import helper

import pytest


@pytest.mark.parametrize(
    "input_fraction, expected_result",
    [((6, 10), (3, 5)), ((84, 12), (7, 1)), ((1024, 9816), (128, 1227))],
)
def test_simplify_fraction(input_fraction, expected_result):
    """Ensure all fraction types simplify correctly"""
    actual = helper.simplify_fraction(input_fraction)
    assert actual == expected_result


@pytest.mark.parametrize(
    "number, expected_result",
    [(123, [123, 231, 312]), (4513, [4513, 5134, 1345, 3451]), (69, [69, 96])],
)
def test_all_rotations(number, expected_result):
    """Ensure all fraction types simplify correctly"""
    actual = helper.all_rotations(number)
    assert actual == expected_result


@pytest.mark.parametrize(
    "base, number, expected_result",
    [(2, 10, 1010), (4, 228, 3210), (7, 100, 202)],
)
def test_base_conversion(base, number, expected_result):
    """Ensure multiple bases convert correctly"""
    actual = helper.base_conversion(base, number)
    assert actual == expected_result


def test_triangle_numbers():
    """returns triangle_numbers"""
    actual = helper.triangle_numbers(10)
    expected = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
    assert actual == expected


@pytest.mark.parametrize(
    "input, expected_result",
    [(21, True), (28, True), (36, True), (42, False)],
)
def test_is_triangle_number(input, expected_result):
    """test of triangle"""
    actual = helper.is_triangle_number(input)
    assert actual == expected_result


@pytest.mark.parametrize(
    "input, expected_result",
    [(4, True), (81, True), (1600, True), (27, False)],
)
def test_is_square_number(input, expected_result):
    """test of squares"""
    actual = helper.is_square_number(input)
    assert actual == expected_result


@pytest.mark.parametrize(
    "input, expected_result",
    [(287, True), (330, True), (376, True), (300, False)],
)
def test_is_pentagonal_number(input, expected_result):
    """test of pentagonal"""
    actual = helper.is_pentagonal_number(input)
    assert actual == expected_result


@pytest.mark.parametrize(
    "input, expected_result",
    [(120, True), (153, True), (190, True), (200, False)],
)
def test_is_hexagonal_number(input, expected_result):
    """test of hexagonal"""
    actual = helper.is_hexagonal_number(input)
    assert actual == expected_result


@pytest.mark.parametrize(
    "input, expected_result",
    [(286, True), (342, True), (403, True), (400, False)],
)
def test_is_heptagonal_number(input, expected_result):
    """test of hexagonal"""
    actual = helper.is_heptagonal_number(input)
    assert actual == expected_result


@pytest.mark.parametrize(
    "input, expected_result",
    [(560, True), (645, True), (736, True), (700, False)],
)
def test_is_octagonal_number(input, expected_result):
    """test of hexagonal"""
    actual = helper.is_octagonal_number(input)
    assert actual == expected_result

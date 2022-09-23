"""helper functions so support Euler problems"""

import math


def simplify_fraction(input: tuple) -> tuple:
    """simply a fraction to return lowest terms possible"""

    fraction = input

    while fraction[0] != fraction[1]:
        maximum = max(fraction)
        minimum = min(fraction)
        fraction = (maximum - minimum, minimum)

    divisor = fraction[0]

    return (int(input[0] / divisor), int(input[1] / divisor))


def all_rotations(input: int) -> list:
    """returns all possible rotations of a number"""

    length = len(str(input))
    tens = 10**length
    value = input
    output = [value]
    i = 1

    while i < length:
        value *= 10
        first_digit = value // tens
        value += first_digit
        value = value - (tens * first_digit)
        output.append(value)
        i += 1

    return output


def base_conversion(base: int, number: int) -> int:
    """convert any number of base10 to any number of baseX"""

    output = ""
    while True:

        int_quotient = int(number / base)
        remainder = number % base
        output = f"{remainder}{output}"

        if int_quotient == 0:
            break

        number = int_quotient

    return int(output)


def triangle_numbers(num: int) -> int:
    """returns n numbers as boolean up to a given number"""
    triangle = [int(0.5 * i * (i + 1)) for i in range(1, num + 1)]

    return triangle


def is_triangle_number(number: int) -> int:
    """returns True if triangle number"""
    return bool((math.sqrt(8 * number + 1) - 1) % 2 == 0)


def is_square_number(number: int) -> int:
    """returns True if square number"""
    return bool(math.sqrt(number) % 1 == 0)


def is_pentagonal_number(number: int) -> int:
    """returns True if pentagonal numbers"""
    return bool((math.sqrt(24 * number + 1) + 1) % 6 == 0)


def is_hexagonal_number(number: int) -> int:
    """returns True if hexagonal numbers"""
    return bool((math.sqrt(8 * number + 1) + 1) % 4 == 0)


def is_heptagonal_number(number: int) -> int:
    """returns True if heptagonal numbers"""
    return bool((math.sqrt(40 * number + 9) + 3) % 10 == 0)


def is_octagonal_number(number: int) -> int:
    """returns True if octagonal numbers"""
    return bool((math.sqrt(3 * number + 1) + 1) % 3 == 0)


if __name__ == "__main__":
    test1 = is_pentagonal_number(40755)
    test2 = is_triangle_number(40755)
    test3 = is_hexagonal_number(40758)
    print(test1, test2, test3)

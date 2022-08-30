"""helper functions so support Euler problems"""


def simplify_fraction(input: tuple) -> tuple:
    """simply a fraction to return lowest terms possible"""

    fraction = input

    while fraction[0] != fraction[1]:
        maximum = max(fraction)
        minimum = min(fraction)
        fraction = (maximum - minimum, minimum)

    divisor = fraction[0]

    return (int(input[0] / divisor), int(input[1] / divisor))

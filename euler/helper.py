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


if __name__ == "__main__":
    test = base_conversion(7, 100)
    print(test)

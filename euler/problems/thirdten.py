"""Project Euler: Problems 21-30"""
import math
import numpy as np

from euler import prime


def problem_twenty_one(num):
    """
    Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
    If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

    For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
    therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

    Evaluate the sum of all the amicable numbers under 10000.
    """
    output = 0

    for a in range(2, num + 1):

        b = sum(prime.divisors(a, True))
        c = sum(prime.divisors(b, True))

        if a == c and a != b:
            output += a

    return output


if __name__ == "__main__":
    test = problem_twenty_one(1000)
    print(test)

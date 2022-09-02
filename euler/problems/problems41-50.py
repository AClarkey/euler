"""Project Euler: Problems 30-39"""

from euler import helper, prime

import math
import time

import numpy as np


def problem_41(numbers: int) -> int:
    """
    We shall say that an n-digit number is pandigital if it makes
    use of all the digits 1 to n exactly once. For example, 2143
    is a 4-digit pandigital and is also prime.

    What is the largest n-digit pandigital prime that exists?
    """
    primes = prime.eratosthenes_sieve_prime(numbers)

    largest_pand = 0

    for i in range(123456789, 1000000000, 2):
        if "0" in str(i):
            continue

        if primes[i]:

            variable = []
            for y in str(i):
                variable.append(y)
            variable = list(set(variable))

            if len(variable) == 9:
                if i > largest_pand:
                    largest_pand = i

    return largest_pand


if __name__ == "__main__":
    start = time.time()

    test = problem_41(1000000000)

    end = time.time()
    runtime = end - start
    print(f"Answer: {test}, Runtime: {'%.3f' % runtime} seconds")

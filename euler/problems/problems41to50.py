"""Project Euler: Problems 41 to 50"""

from euler import helper, prime

import math
import time

import numpy as np


def problem_41(start: int) -> int:
    """
    We shall say that an n-digit number is pandigital if it makes
    use of all the digits 1 to n exactly once. For example, 2143
    is a 4-digit pandigital and is also prime.

    What is the largest n-digit pandigital prime that exists?
    """
    primes = prime.eratosthenes_sieve_prime(start * 100)  # 7750000
    pand_prime = []
    n = start

    while True:
        if primes[n]:
            length = len(str(n))
            count = 0
            for i in range(1, length + 1):
                if str(i) in str(n):
                    count += 1
                if count == length:
                    pand_prime.append(n)

        if n > start * 10:  # 7654325
            break

        n += 2

    return max(pand_prime)


if __name__ == "__main__":
    start = time.time()

    test = problem_41(1001)

    end = time.time()
    runtime = end - start
    print(f"Answer: {test}, Runtime: {'%.3f' % runtime} seconds")

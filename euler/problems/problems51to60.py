"""Project Euler: Problems 41 to 50"""
import time
import string
import math
import itertools

import statistics
from statistics import mode


from euler import helper, prime


def problem_51():
    """
    By replacing the 1st digit of the 2-digit number *3, it turns out that
    six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

    By replacing the 3rd and 4th digits of 56**3 with the same digit, this
    5-digit number is the first example having seven primes among the ten
    generated numbers, yielding the family:
    56003, 56113, 56333, 56443, 56663, 56773, and 56993.
    Consequently 56003, being the first member of this family, is the smallest prime with this property.

    Find the smallest prime which, by replacing part of the number
    (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
    """
    primes = prime.eratosthenes_sieve_prime(100000)

    choose = itertools.combinations(range(5), 2)
    max = 0

    for i in choose:
        for y in range(56000, 57000):
            if primes[y]:
                common = []

                for b in range(0, 10):
                    temp = list(str(y))
                    for a in i:
                        temp[a] = str(b)
                    if primes[int("".join(temp))]:
                        common.append("".join(temp))
                if len(common) == 7:
                    print("DONE", y, i)
                    break


if __name__ == "__main__":
    # start = time.time()

    problem_51()

    # end = time.time()
    # runtime = end - start
    # print(f"Answer: {answer}, Runtime: {'%.3f' % runtime} seconds")

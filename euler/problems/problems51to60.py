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
    primes = prime.eratosthenes_sieve_prime(1000)

    choose = itertools.combinations(range(2), 1)
    # print(next(choose))
    # print(next(choose))

    max = 0

    for i in choose:
        common = []
        for y in range(10, 100):
            if primes[y]:
                for a in i:
                    # needs to be tweaked so all the indexes in the specific i are removed, not just one at a time.
                    temp = list(str(y))
                    temp[a] = ""
                    test = "".join(temp)
                    common.append(test)

                most_common = mode(common)
                counter = common.count(most_common)
                if counter > max:
                    max = counter
                    print(i, most_common, counter)


if __name__ == "__main__":
    # start = time.time()

    problem_51()

    # end = time.time()
    # runtime = end - start
    # print(f"Answer: {answer}, Runtime: {'%.3f' % runtime} seconds")

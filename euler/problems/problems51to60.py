"""Project Euler: Problems 41 to 50"""
import time
import string
import math
import itertools

import statistics
from statistics import mode


from euler import helper, prime


def problem_51(length: int, choose: int, target: int):
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
    upper = 10 ** (length)
    lower = upper // 10

    primes = prime.eratosthenes_sieve_prime(upper)

    choose = itertools.combinations(range(length), choose)
    max = 0

    for i in choose:
        for y in range(lower, upper):
            if primes[y]:
                common = []

                for b in range(0, 10):
                    temp = list(str(y))
                    for a in i:
                        temp[a] = str(b)
                    if primes[int("".join(temp))]:
                        common.append("".join(temp))

                if len(common) == target:
                    if common[0][1] != "0":
                        output = common[0]
                    break
    return output


def problem_52(factors: int) -> int:
    """
    It can be seen that the number, 125874, and its double, 251748,
    contain exactly the same digits, but in a different order.
    Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
    """

    def list_of_digits(num: int) -> list:
        """returns a list of digits"""
        digits = list(str(num))
        digits.sort()
        return digits

    n = 1
    while True:
        flag = True
        for i in range(2, factors + 1):
            if list_of_digits(n) != list_of_digits(n * i):
                flag = False
                break
        if flag:
            break
        n += 1

    return n


if __name__ == "__main__":
    start = time.time()

    answer = problem_52(6)

    end = time.time()
    runtime = end - start
    print(f"Answer: {answer}, Runtime: {'%.3f' % runtime} seconds")

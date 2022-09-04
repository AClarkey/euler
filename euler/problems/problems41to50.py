"""Project Euler: Problems 41 to 50"""

from euler import helper, prime

import math
import time
import string

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


def problem_42(datafile: str) -> int:
    """
    The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:
    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
    By converting each letter in a word to a number corresponding to its alphabetical position and adding these
    values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word
    value is a triangle number then we shall call the word a triangle word.
    """
    numbers = helper.triangle_numbers(50)
    triangle_numbers = []
    with open(f"./data/{datafile}", "r") as file:
        input = file.read()

    words = input.replace("\n", " ").replace('"', "").split(",")

    for i in words:
        value = 0
        for y in i:
            value += string.ascii_uppercase.index(y) + 1
        if value in numbers:
            triangle_numbers.append(value)

    return len(triangle_numbers)


if __name__ == "__main__":
    start = time.time()

    test = problem_42("p042_words.txt")

    end = time.time()
    runtime = end - start
    print(f"Answer: {test}, Runtime: {'%.3f' % runtime} seconds")

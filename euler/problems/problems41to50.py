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


def problem_43() -> int:
    """
    The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the
    digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

    Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

    Find the sum of all 0 to 9 pandigital numbers with this property.
    """

    divisors = [3, 5, 7, 11, 13, 17]

    numbers = []
    for i in range(1, 10):
        for y in range(1000):

            if y % 2 == 0:
                value = f"{i}{str(y).zfill(3)}"
                pand_value = list(set([z for z in value]))
                if len(value) == len(pand_value):
                    numbers.append(value)

    input_numbers = numbers
    start = 2

    for x in divisors:

        new_numbers = []

        for i in input_numbers:
            digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            for y in i:
                digits.remove(int(y))

            for z in digits:
                value = f"{i}{z}"[start : start + 4]

                if int(value) % x == 0:
                    new_numbers.append(f"{i}{z}")

        input_numbers = new_numbers
        start += 1

    return sum(int(i) for i in input_numbers)


if __name__ == "__main__":
    # start = time.time()

    answer = problem_43()

    # end = time.time()
    # runtime = end - start
    # print(f"Answer: {answer}, Runtime: {'%.3f' % runtime} seconds")

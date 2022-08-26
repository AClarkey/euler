"""Project Euler: Problems 21-30"""
import math
from decimal import Decimal, getcontext

import re
import numpy as np
import csv
import string
import itertools
import copy
import sympy


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


def problem_twenty_two(datafile: str) -> int:
    """
    Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
    begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this
    value by its alphabetical position in the list to obtain a name score.
    For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
    is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
    What is the total of all the name scores in the file?
    """
    output = 0

    with open(f"./data/{datafile}", "r") as file:
        input = file.read()

    names = input.replace("\n", " ").replace('"', "").split(",")
    names.sort()

    letters = list(string.ascii_uppercase)

    for i in range(0, len(names)):
        word_value = 0
        for y in names[i]:
            word_value += letters.index(y) + 1
        output += word_value * (i + 1)

    return output


def problem_twenty_three(num: int) -> int:
    """
    A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
    For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
    which means that 28 is a perfect number.
    A number n is called deficient if the sum of its proper divisors is less than n and it is called
    abundant if this sum exceeds n.
    As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be
    written as the sum of two abundant numbers is 24.

    By mathematical analysis, it can be shown that all integers greater than 28123 can be written
    as the sum of two abundant numbers.

    However, this upper limit cannot be reduced any further by analysis even though it is known that
    the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

    Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
    """
    abundant = [i for i in range(12, num) if sum(prime.divisors(i, True)) > i]
    numbers = [True] * num

    for x in abundant:
        for y in abundant[0 : abundant.index(x) + 1]:
            z = x + y
            if z < num + 1 and numbers[z - 1] == True:
                numbers[z - 1] = False

    output = 0
    for i in range(0, num):
        if numbers[i]:
            output += i + 1

    return output


def problem_twenty_four(num: str, position: int) -> str:
    """
    A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation
    of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically,
    we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
    012   021   102   120   201   210
    What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
    """
    number = [i for i in num]

    perm = list(itertools.permutations(number))
    perm.sort()
    perm_final = perm[position - 1]

    output = ""
    for i in perm_final:
        output += i
    return output


def problem_twenty_five(num: int) -> int:
    """
    The Fibonacci sequence is defined by the recurrence relation:
    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
    Hence the first 12 terms will be:
    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144
    The 12th term, F12, is the first term to contain three digits.
    What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
    """
    f1 = 1
    f2 = 1
    i = 2

    while True:
        if len(str(f2)) < num:
            f3 = f1 + f2  # 3
            f1 = f2  # 2
            f2 = f3  # 3
            i += 1
        else:
            break
    return i


def problem_twenty_six(numbers: int) -> int:
    """
    A unit fraction contains 1 in the numerator. The decimal representation of the unit
    fractions with denominators 2 to 10 are given:

    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10	= 	0.1
    Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen
    that 1/7 has a 6-digit recurring cycle.

    Find the value of d < 1000 for which 1/d contains the longest recurring cycle in
    its decimal fraction part.
    """
    output = {}
    index = 0

    for i in range(2, numbers):

        decimals = []
        divisor = i
        remainder = 1
        dividend = 1

        while remainder != 0 and len(decimals) < (numbers * 2) + 1:

            quotient = math.floor(dividend / divisor)
            decimals.append(quotient)
            remainder = dividend % divisor
            dividend = remainder * 10

        number = ""
        for y in range(0, len(decimals)):
            number += str(decimals[y])

        number = number.lstrip("0")

        pattern = re.compile(r"(.+?)\1+")
        sequence = re.findall(pattern, number)

        if sequence == []:
            sequence_length = 0
        else:
            sequence_length = len(max(sequence, key=len))
            if sequence_length > index:
                index = i
        output[i] = sequence
    return index


def problem_twenty_seven(numbers: int) -> int:
    """
    Find the product of the coefficients,  and , for the quadratic expression that produces
    the maximum number of primes for consecutive values of , starting with n = 0.
    """
    val_a = prime.eratosthenes_sieve_prime(numbers)
    set_a = [i for i in range(numbers) if val_a[i]]

    value = 0

    for a in set_a:
        for b in set_a:

            n = 0

            while prime.is_prime(n**2 + a * n + b):
                n += 1

            if n > value:

                value = n
                axb = a * b

            n = 0
            while prime.is_prime(n**2 - a * n + b):
                n += 1

            if n > value:

                value = n
                axb = -1 * a * b

    return axb


if __name__ == "__main__":
    test = problem_twenty_seven(10)
    print(test)

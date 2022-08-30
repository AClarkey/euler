"""Project Euler: Problems 30-39"""

from euler import helper

import math
from decimal import Decimal, getcontext

import re
import numpy as np
import csv
import string
import itertools
import copy


from euler import prime


def problem_thirty_one(coins: list, total: int) -> int:
    """
    How many different ways can £2 be made using any number of coins?
    """
    number_coins = len(coins)
    a = np.zeros((number_coins, total + 1), dtype=int)

    for i in range(0, number_coins):
        for j in range(0, total + 1):

            if j == 0:
                a[i][j] = 1

            if i == 0:
                if j % coins[i] == 0:
                    a[i][j] = 1

            else:
                if coins[i] > total:
                    a[i][j] = a[i - 1][j]
                else:
                    a[i][j] = a[i - 1][j] + a[i][j - coins[i]]

    return a[-1, -1]


def problem_thirty_two() -> int:
    """
    Find the sum of all products whose multiplicand/multiplier/product
    identity can be written as a 1 through 9 pandigital.
    """
    products = []

    for i in range(1, 100):

        if "0" in str(i):
            continue

        for y in range(1, 10000):

            if "0" in str(y):
                continue

            for x in str(i):
                if x in str(y):
                    continue

            variable = []
            product = i * y

            if "0" in str(product):
                continue

            total = f"{i}{y}{product}"

            if len(total) == 9:
                for z in total:
                    variable.append(z)

                variable = list(set(variable))

                if len(variable) == 9:
                    products.append(product)

    return sum(list(set(products)))


def problem_thirty_three(numbers: int) -> int:
    """
    There are exactly four non-trivial examples of this type of fraction,
    less than one in value, and containing two digits in the numerator and denominator.

    If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
    """
    nom = []
    denoms = []

    for i in range(10, numbers):
        for y in range(10, numbers):
            if i == y or i == int(str(y)[::-1]) or "0" in str(i) or "0" in str(y):
                continue

            value_before = i / y

            for z in str(i):
                if z in str(y):
                    num = str(i).replace(z, "")
                    denom = str(y).replace(z, "")
                    if num == "":
                        num = z
                    if denom == "":
                        denom = z
                    value_after = int(num) / int(denom)
                else:
                    value_after = 0

            if value_before == value_after:
                nom.append(i)
                denoms.append(y)

    final_denom = 1
    for i in denoms:
        final_denom *= i
    final_num = 1
    for i in nom:
        final_num *= i

    return helper.simplify_fraction((final_num, final_denom))[1]


if __name__ == "__main__":
    test = problem_thirty_three(100)
    print(test)

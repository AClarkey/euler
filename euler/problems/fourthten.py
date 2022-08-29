"""Project Euler: Problems 30-39"""

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


if __name__ == "__main__":
    test = problem_thirty_one([2, 3, 5, 10], 100)

    print(test)

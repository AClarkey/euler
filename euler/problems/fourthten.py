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


def problem_thirty_one(number: int) -> int:
    """
    How many different ways can £2 be made using any number of coins?
    """

    # coins = [1, 2, 5, 10, 20, 50, 100, 200]
    combo = []

    combo.append([1, 0, 0, 0, 0])
    combo.append([0, 2, 0, 0, 0])
    combo.append([0, 0, 4, 0, 0])
    combo.append([0, 0, 0, 10, 0])
    combo.append([0, 0, 0, 0, 20])

    for coin_100 in range(2):
        for coin_50 in range(4):
            for coin_20 in range(10):
                for coin_10 in range(20):
                    for coin_5 in range(40):
                        for coin_2 in range(100):
                            for coin_1 in range(200):
                                if (
                                    100 * coin_100
                                    + 50 * coin_50
                                    + 20 * coin_20
                                    + 10 * coin_10
                                    + 5 * coin_5
                                    + 2 * coin_2
                                    + 1 * coin_1
                                    == 200
                                ):
                                    combo.append(
                                        [
                                            0,
                                            coin_100,
                                            coin_50,
                                            coin_20,
                                            coin_10,
                                            coin_5,
                                            coin_2,
                                            coin_1,
                                        ]
                                    )

    return combo


def play():
    a = [1, 2, 5, 10, 20, 50, 100, 200]

    w = 200

    # 1. Exclude the coin
    # 2. Include the coin
    # add 1. and 2. 
    # time complexity is exponential with recursion, dynamic is stored. 

    # https://www.youtube.com/watch?v=L27_JpN6Z1Q

    total = 1
    for i in a:
        total = total * (1/)




if __name__ == "__main__":
    test = problem_thirty_one(200)
    print(len(test))
    # print(test)

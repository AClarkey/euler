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

    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    combo = []

    for coin_200 in range(1 + 1):
        for coin_100 in range(2 + 1):
            for coin_50 in range(4 + 1):
                for coin_20 in range(10 + 1):
                    for coin_10 in range(20 + 1):
                        for coin_5 in range(40 + 1):
                            for coin_2 in range(100 + 1):
                                for coin_1 in range(200 + 1):
                                    if (
                                        200 * coin_200
                                        + 100 * coin_100
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
                                                coin_200,
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


if __name__ == "__main__":
    test = problem_thirty_one(200)
    print(len(test))

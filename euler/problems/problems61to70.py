"""Project Euler: Problems 61 to 70"""
import time
import string
import math
import itertools

import statistics
from statistics import mode
from tkinter.filedialog import test


from euler import helper, prime


def problem_61(number: int) -> int:
    """
    Find the sum of the only ordered set of six cyclic 4-digit numbers for
    which each polygonal type: triangle, square, pentagonal, hexagonal,
    heptagonal, and octagonal, is represented by a different number in the set.
    """

    test = helper.is_heptagonal_number(34)
    print(test)


if __name__ == "__main__":
    start = time.time()

    answer = problem_61(10)

    end = time.time()
    runtime = end - start
    print(f"Answer: {answer}, Runtime: {'%.3f' % runtime} seconds")

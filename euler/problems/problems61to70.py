"""Project Euler: Problems 61 to 70"""
from re import I
import time
import string
import math
import itertools
import copy

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

    numbers = set()
    for i in range(1000, 10000):
        if helper.is_triangle_number(i):
            numbers.add(i)
        if helper.is_square_number(i):
            numbers.add(i)
        if helper.is_pentagonal_number(i):
            numbers.add(i)
        if helper.is_hexagonal_number(i):
            numbers.add(i)
        if helper.is_heptagonal_number(i):
            numbers.add(i)
        if helper.is_octagonal_number(i):
            numbers.add(i)

    # print(len(numbers), sorted(numbers))
    output = []

    for i in numbers:
        for y in numbers:
            if str(i)[len(str(i)) - 2 :] == str(y)[0:2]:
                output.append(int(str(i) + str(y)))
    output2 = []
    for i in output:
        for y in numbers:
            if str(i)[len(str(i)) - 2 :] == str(y)[0:2]:
                output2.append(int(str(i) + str(y)))
    output3 = []
    for i in output2:
        for y in numbers:
            if str(i)[len(str(i)) - 2 :] == str(y)[0:2]:
                output3.append(int(str(i) + str(y)))
    output4 = []
    for i in output3:
        for y in numbers:
            if str(i)[len(str(i)) - 2 :] == str(y)[0:2]:
                output4.append(int(str(i) + str(y)))
    output = []
    for i in output4:
        last_digit = int(str(i)[len(str(i)) - 2 :] + str(i)[0:2])
        if last_digit in numbers:
            output.append(int(str(i) + str(last_digit)))

    for var in output:
        numbers = []
        for i in range(0, 24, 4):
            numbers.append(str(var)[i : i + 4])
        if len(list(set(numbers))) == 6:
            print(numbers)
        else:
            output.remove(var)

        for y in numbers: 


if __name__ == "__main__":
    # start = time.time()

    answer = problem_61(10)

    # end = time.time()
    # runtime = end - start
    # # print(f"Answer: {answer}, Runtime: {'%.3f' % runtime} seconds")

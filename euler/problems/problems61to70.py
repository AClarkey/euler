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


def problem_61() -> int:
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

    def is_type(var, lists) -> list:
        if helper.is_triangle_number(var):
            lists[0] += 1
        if helper.is_square_number(var):
            lists[1] += 1
        if helper.is_pentagonal_number(var):
            lists[2] += 1
        if helper.is_hexagonal_number(var):
            lists[3] += 1
        if helper.is_heptagonal_number(var):
            lists[4] += 1
        if helper.is_octagonal_number(var):
            lists[5] += 1
        return lists

    results = set()

    for var in output:
        final = []
        check = [0, 0, 0, 0, 0, 0]
        sum = 0
        for i in range(0, 24, 4):
            digit = str(var)[i : i + 4]
            final.append(digit)
            sum += int(digit)
        if len(list(set(final))) != 6:
            output.remove(var)

        for y in final:
            check = is_type(int(y), check)

        if check.count(0) == 0:
            results.add(sum)

    return results


def problem_62(num: int) -> int:
    """
    Find the smallest cube for which exactly five permutations of its digits are cube.
    """

    d = {}
    for i in range(10000):
        c = i**3
        d.setdefault("".join(sorted(str(c))), set()).add(c)
    return min(sorted(v) for v in d.values() if len(v) == num)[0]


if __name__ == "__main__":
    start = time.time()

    answer = problem_62(3)

    end = time.time()
    runtime = end - start
    print(f"Answer: {answer}, Runtime: {'%.3f' % runtime} seconds")

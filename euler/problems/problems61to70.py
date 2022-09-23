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

    def is_type(number: int, types: list) -> list:
        if helper.is_triangle_number(number):
            types[0] += 1
        if helper.is_square_number(number):
            types[1] += 1
        if helper.is_pentagonal_number(number):
            types[2] += 1
        if helper.is_hexagonal_number(number):
            types[3] += 1
        if helper.is_heptagonal_number(number):
            types[4] += 1
        if helper.is_octagonal_number(number):
            types[5] += 1
        return types

    for one in range(1000, 10000):
        types = [0, 0, 0, 0, 0, 0]
        if is_type(one, types).count(1) == 1:

            one_end = str(one)[2:4]
            for b in range(10, 100):
                two = one_end + str(b)
                if is_type(int(two), types).count(1) == 2:

                    two_end = str(two)[2:4]
                    for c in range(10, 100):
                        three = two_end + str(c)
                        if is_type(int(three), types).count(1) == 3:

                            three_end = str(three)[2:4]
                            for d in range(10, 100):
                                four = three_end + str(d)
                                if is_type(int(four), types).count(1) == 4:

                                    four_end = str(four)[2:4]
                                    for e in range(10, 100):
                                        five = four_end + str(e)
                                        if is_type(int(five), types).count(1) == 5:

                                            five_end = str(five)[2:4]
                                            six = five_end + str(one)[0:2]
                                            if is_type(int(six), types).count(1) == 6:
                                                print(
                                                    one,
                                                    two,
                                                    three,
                                                    four,
                                                    five,
                                                    six,
                                                    is_type(int(six), types),
                                                )


if __name__ == "__main__":
    # start = time.time()

    answer = problem_61(10)

    # end = time.time()
    # runtime = end - start
    # # print(f"Answer: {answer}, Runtime: {'%.3f' % runtime} seconds")
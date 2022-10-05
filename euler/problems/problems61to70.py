"""Project Euler: Problems 61 to 70"""
import time
import string
import math
import itertools
import copy
import decimal
import re


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

    output = {}

    for i in range(10000):
        cube = i**3
        output.setdefault("".join(sorted(str(cube))), set()).add(cube)

    return min(sorted(v) for v in output.values() if len(v) == num)[0]


def problem_63() -> int:
    """
    The 5-digit number, 16807=7**5, is also a fifth power. Similarly, the 9-digit number, 134217728=8**9, is a ninth power.

    How many n-digit positive integers exist which are also an nth power?
    """
    counter = 0
    for base in range(1, 10):
        for exp in range(1, 22):
            value = base**exp
            if len(str(value)) == exp:
                counter += 1
    return counter


def problem_64(num: int) -> int:
    """
    Exactly four continued fractions, for N <= 13, have an odd period.
    How many continued fractions for N <= 10,000 have an odd period?

    Struggled, credit to: https://radiusofcircle.blogspot.com/2016/11/project-euler-problem-64-solution-with-python.html
    """

    def cont_fraction(n):

        mn = 0.0
        dn = 1.0
        a0 = int(math.sqrt(n))
        an = int(math.sqrt(n))
        period = 0

        if a0 != (math.sqrt(n)):
            while an != 2 * a0:

                # print(
                #     f"n: {n}, a0: {a0}, mn: {mn}, dn: {dn}, an: {an}, period: {period}"
                # )

                mn = dn * an - mn
                dn = (n - mn**2) / dn
                an = int((a0 + mn) / dn)
                period += 1

        # print(f"n: {n}, a0: {a0}, mn: {mn}, dn: {dn}, an: {an}, period: {period}")
        return period

    counter = 0
    for i in range(2, num):

        if cont_fraction(i) % 2 == 1:
            counter += 1

    return counter


def problem_65(num: int) -> int:
    """
    Find the sum of digits in the numerator of the 100th convergent of the continued fraction for .
    """

    def cont_fraction(n):

        mn = 0.0
        dn = 1.0
        a0 = int(math.sqrt(n))
        an = int(math.sqrt(n))
        period = 0

        if a0 != (math.sqrt(n)):
            while an != 2 * a0:

                print(
                    f"n: {n}, a0: {a0}, mn: {mn}, dn: {dn}, an: {an}, period: {period}"
                )

                mn = dn * an - mn
                dn = (n - mn**2) / dn
                an = int((a0 + mn) / dn)
                period += 1

        print(f"n: {n}, a0: {a0}, mn: {mn}, dn: {dn}, an: {an}, period: {period}")
        return period

    print(2 + 1 / (1 + 1 / (2)))


if __name__ == "__main__":
    start = time.time()

    answer = problem_65(10)

    end = time.time()
    runtime = end - start
    print(f"Answer: {answer}, Runtime: {'%.3f' % runtime} seconds")

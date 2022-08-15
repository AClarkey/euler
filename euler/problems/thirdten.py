"""Project Euler: Problems 21-30"""
from bz2 import compress
import math
import numpy as np
import csv
import string

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


if __name__ == "__main__":
    test = problem_twenty_three(100)
    print(test)

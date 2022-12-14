"""Project Euler: Problems 31-40"""
import math
import time

import numpy as np


from euler import helper, prime


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


def problem_thirty_four(numbers: int) -> int:
    """Find the sum of all numbers which are equal to the sum of the factorial of their digits."""

    def max():
        number = 1
        fact9 = math.factorial(9)
        while number * fact9 > 10 ** (number - 1):
            number += 1

        return 10 ** (number - 1)

    # max = 1000000. Smallest 8 digit number > 8 * 9!

    total = 0
    factors = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

    for i in range(3, numbers):

        if i == sum(factors[int(n)] for n in str(i)):

            total += i

    return total


def problem_thirty_five(numbers: int) -> int:
    """The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
    There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
    How many circular primes are there below one million?
    """
    circular = []

    for i in range(3, numbers, 2):
        st = str(id)
        if "2" in st or "4" in st or "6" in st or "8" in st or "5" in st or "0" in st:
            continue
        if not prime.is_prime(i):
            continue

        stop = False

        rotation = helper.all_rotations(i)

        for y in rotation:
            if not prime.is_prime(y):
                stop = True
                continue
        if stop:
            continue
        else:
            circular.append(i)
    circular.append(2)

    return len(circular)


def problem_thirty_six(base: int, numbers: int) -> int:
    """The decimal number, 585 = 1001001001, base2 (binary), is palindromic in both bases.
    Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
    (Please note that the palindromic number, in either base, may not include leading zeros.)
    """

    double_base = []

    for i in range(1, numbers, 2):

        base_number = helper.base_conversion(base, i)

        if i == int(str(i)[::-1]):
            if base_number == int(str(base_number)[::-1]):
                double_base.append(i)

    return sum(double_base)


def problem_thirty_seven(numbers: int) -> int:
    """
    The number 3797 has an interesting property. Being prime itself, it is possible
    to continuously remove digits from left to right, and remain prime at each stage:

    3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

    Find the sum of the only eleven primes that are both truncatable from left to
    right and right to left.
    NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
    """

    trunc = []
    primes = prime.eratosthenes_sieve_prime(numbers)

    for i in range(11, numbers):
        flag = True

        if not primes[i]:
            continue

        if i % 10 == 1 or int(str(i)[0]) in [1, 4, 6, 8]:
            continue

        if "0" in str(i) or "4" in str(i) or "6" in str(i) or "8" in str(i):
            continue

        length = len(str(i))  # 2

        for y in range(length - 1):
            right = str(i)[0 : length - y - 1]
            left = str(i)[0 + y + 1 : length]
            if not primes[int(right)] or not primes[int(left)]:
                flag = False
                continue

        if flag:
            trunc.append(i)

    return sum(trunc)


def problem_thirty_eight() -> int:
    """
    What is the largest 1 to 9 pandigital 9-digit number that can be formed
    as the concatenated product of an integer with (1,2, ... , n) where n > 1?
    """
    pand = []

    number = 2
    integer = 1

    product_length = ""

    while number < 10000:

        if len(product_length) < 9:
            if "0" in product_length:
                number += 1
                product_length = ""
                integer = 1
            else:
                product = number * integer
                product_length += str(product)
                integer += 1

        if len(product_length) > 9:
            number += 1
            product_length = ""
            integer = 1

        if len(product_length) == 9:
            if "0" in product_length:
                number += 1
                product_length = ""
                integer = 1
            else:
                list_num = []
                for z in product_length:
                    list_num.append(z)
                length = list(set(list_num))
                if len(length) == 9:
                    pand.append(product_length)
                    number += 1
                    product_length = ""
                else:
                    number += 1
                    product_length = ""
                    integer = 1

    return int(max(pand))


def problem_thirty_nine(numbers: int) -> int:
    """
    If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

    {20,48,52}, {24,45,51}, {30,40,50}

    For which value of p ≤ 1000, is the number of solutions maximised?
    """
    solutions = {key: 0 for key in list(range(1, numbers * 5))}

    for a in range(1, numbers):  # 1,
        for b in range(a, numbers):
            c = math.sqrt(a**2 + b**2)
            if c % 1 != 0:
                continue
            c = int(c)

            perimeter = a + b + c

            if perimeter > 1000:
                continue

            solutions[perimeter] += 1

    most_solutions = 0

    for key, value in solutions.items():
        if value != 0:
            if value > most_solutions:

                most_solutions = value
                output = key

    return output


def problem_forty(numbers: int) -> int:
    """
    An irrational decimal fraction is created by concatenating the positive integers:
    0.123456789101112131415161718192021...
    It can be seen that the 12th digit of the fractional part is 1.
    If dn represents the nth digit of the fractional part, find the value of the following expression.
    d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

    numbers = 10 ** numbers - 1 digits to go to.
    """

    index_to_find = []
    for i in range(numbers):
        index_to_find.append(10**i)

    new_length = 0
    old_length = 0
    i = 0
    digits = []

    while new_length < 10**numbers:

        if new_length >= index_to_find[0]:
            index = index_to_find[0] - old_length
            digits.append(int(str(i)[index - 1]))
            index_to_find.pop(0)

            if index_to_find == []:
                break

        i += 1
        old_length = new_length
        new_length += len(str(i))

    return np.prod(digits)


if __name__ == "__main__":
    start = time.time()

    test = problem_forty(6)
    # print(test)

    end = time.time()
    runtime = end - start
    print(f"Answer: {test}, Runtime: {'%.3f' % runtime} seconds")

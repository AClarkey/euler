"""Project Euler: Problems 41 to 50"""
import time
import string
import math


from euler import helper, prime


def problem_41(start: int) -> int:
    """
    We shall say that an n-digit number is pandigital if it makes
    use of all the digits 1 to n exactly once. For example, 2143
    is a 4-digit pandigital and is also prime.

    What is the largest n-digit pandigital prime that exists?
    """
    primes = prime.eratosthenes_sieve_prime(start * 100)  # 7750000
    pand_prime = []
    n = start

    while True:
        if primes[n]:
            length = len(str(n))
            count = 0
            for i in range(1, length + 1):
                if str(i) in str(n):
                    count += 1
                if count == length:
                    pand_prime.append(n)

        if n > start * 10:  # 7654325
            break

        n += 2

    return max(pand_prime)


def problem_42(datafile: str) -> int:
    """
    The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:
    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
    By converting each letter in a word to a number corresponding to its alphabetical position and adding these
    values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word
    value is a triangle number then we shall call the word a triangle word.
    """
    numbers = helper.triangle_numbers(50)
    triangle_numbers = []
    with open(f"./data/{datafile}", "r") as file:
        input = file.read()

    words = input.replace("\n", " ").replace('"', "").split(",")

    for i in words:
        value = 0
        for y in i:
            value += string.ascii_uppercase.index(y) + 1
        if value in numbers:
            triangle_numbers.append(value)

    return len(triangle_numbers)


def problem_43() -> int:
    """
    The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the
    digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

    Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

    Find the sum of all 0 to 9 pandigital numbers with this property.
    """

    divisors = [3, 5, 7, 11, 13, 17]

    numbers = []
    for i in range(1, 10):
        for y in range(1000):

            if y % 2 == 0:
                value = f"{i}{str(y).zfill(3)}"
                pand_value = list(set([z for z in value]))
                if len(value) == len(pand_value):
                    numbers.append(value)

    input_numbers = numbers
    start = 2

    for x in divisors:

        new_numbers = []

        for i in input_numbers:
            digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            for y in i:
                digits.remove(int(y))

            for z in digits:
                value = f"{i}{z}"[start : start + 4]

                if int(value) % x == 0:
                    new_numbers.append(f"{i}{z}")

        input_numbers = new_numbers
        start += 1

    return sum(int(i) for i in input_numbers)


def problem_44() -> int:
    """
    Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten pentagonal numbers are:
    1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
    It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 − 22 = 48, is not pentagonal.

    Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and
    D = |Pk − Pj| is minimised; what is the value of D?
    """
    i = 1
    flag = True
    while flag:
        for y in range(1, i):
            k = i * (3 * i - 1) // 2
            j = y * (3 * y - 1) // 2
            if helper.is_pentagonal_number(k + j) and helper.is_pentagonal_number(
                k - j
            ):
                output = k - j
                flag = False
        i += 1
    return output


def problem_45(start: int) -> int:
    """
    Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

    Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
    Pentagonal	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
    Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
    It can be verified that T285 = P165 = H143 = 40755.

    Find the next triangle number that is also pentagonal and hexagonal.
    """

    i = start

    while True:
        i += 1
        tri = (i * (i + 1)) // 2

        if helper.is_hexagonal_number(tri):
            if helper.is_pentagonal_number(tri):
                break

    return tri


def problem_46():
    """
    It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

    9 = 7 + 2×12
    15 = 7 + 2×22
    21 = 3 + 2×32
    25 = 7 + 2×32
    27 = 19 + 2×22
    33 = 31 + 2×12

    It turns out that the conjecture was false.

    What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
    """
    primes = prime.eratosthenes_sieve_prime(10000)
    primes_list = [i for i in range(1, 10000) if primes[i]]

    def is_twice_square(number: int) -> int:
        """checks if a number can be written as twice a square or not"""
        return float.is_integer(math.sqrt(number / 2))

    value = 9
    while True:

        if not primes[value]:

            flag = False
            primes_less = [i for i in primes_list if i < value]

            for y in primes_less:
                number = value - y

                if is_twice_square(number):
                    flag = True
                    break

            if not flag:
                break

        value += 2

    return value


def problem_47(number: int) -> int:
    """
    The first two consecutive numbers to have two distinct prime factors are:
    14 = 2 × 7
    15 = 3 × 5
    The first three consecutive numbers to have three distinct prime factors are:
    644 = 2² × 7 × 23
    645 = 3 × 5 × 43
    646 = 2 × 17 × 19.
    Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
    """
    i = 1
    flag = False
    primes = prime.eratosthenes_sieve_prime(1000000)

    while True:

        factors_set = []
        count = 0

        if primes[i]:
            i += 1
            continue

        for y in range(i, i + number + 1):

            count += 1

            if primes[y]:
                break

            p_factors = prime.prime_factors(y)

            if len(p_factors) < number:
                break

            dict = {y: p_factors.count(y) for y in set(p_factors)}

            p_factors = []
            for key, value in dict.items():
                p_factors.append(key**value)

            if len(p_factors) == number:
                factors_set.append(p_factors)

        if len(factors_set) == number:
            distinct = []
            for a in factors_set:
                for b in a:
                    distinct.append(b)

            if len(set(distinct)) == number**2:
                flag = True
                print(i, factors_set)
                break

        if flag:
            break

        i += count

    return i


def problem_47b():
    """alternative solution to above"""
    for i in range(50000, 1000000):
        if len(prime.distinct_prime_factors(i)) == 4:
            if len(prime.distinct_prime_factors(i + 1)) == 4:
                if len(prime.distinct_prime_factors(i + 2)) == 4:
                    if len(prime.distinct_prime_factors(i + 3)) == 4:
                        print(i)
                        break


if __name__ == "__main__":
    start = time.time()

    answer = problem_47b()

    # print(answer)
    end = time.time()
    runtime = end - start
    print(f"Answer: {answer}, Runtime: {'%.3f' % runtime} seconds")

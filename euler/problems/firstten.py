"""Project Euler: Problems 1-10"""
from euler import prime

import math


def problem_one(num):
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000.
    """
    output = 0
    for i in range(1, num):
        if i % 3 == 0 or i % 5 == 0:
            output += i
    return output


def problem_two(num):
    """
    Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
    By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
    """
    var1 = 1
    var2 = 2
    output = 0
    while var2 < num:
        if var2 % 2 == 0:
            output += var2
        var2 += var1
        var1 = var2 - var1
    return output


def problem_three(num):
    """
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143?
    """
    output = prime.prime_factors(num)
    return output[-1]


def problem_four(num):
    """
    A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
    Find the largest palindrome made from the product of two 3-digit numbers.
    """
    length = ""
    for i in range(1, num + 1):
        length += "9"
    output = max(
        i * y
        for i in range(1, int(length) + 1)
        for y in range(1, int(length) + 1)
        if str(i * y) == str(i * y)[::-1]
    )
    return output


def problem_five(num: int):
    """
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
    """

    factors = [prime.prime_factors(i) for i in range(1, num + 1)]
    used = []
    output = []
    print(factors)
    for i in reversed(factors):
        if len(i) > 1 and len(set(i)) == 1:
            for y in i:
                if y not in used:
                    output.append(y)
            used.append(i[0])

        if len(i) == 1 and i[0] not in used:
            output.append(i[0])

    return math.prod(output)


def problem_six(num):
    """
    The sum of the squares of the first ten natural numbers is,
    1^2 + ... + 10^2 = 385
    The square of the sum of the first ten natural numbers is,
    (1+2+...+10)^2 = 3025
    Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is,
    3025-385 = 2640
    Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
    """
    sum_sq = 0
    sq_sum = 0
    for i in range(1, num + 1):
        sum_sq += i * i
        sq_sum += i
    sq_sum *= sq_sum
    return abs(sum_sq - sq_sum)


def problem_seven(num):
    """
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
    What is the 10 001st prime number?
    """
    i = 0
    output = 1

    while i < num:
        output += 1
        while not prime.is_prime(output):
            output += 1
        i += 1
    return output


def problem_eight(num):
    """
    The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
    Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
    """
    series = """73167176531330624919225119674426574742355349194934
    96983520312774506326239578318016984801869478851843
    85861560789112949495459501737958331952853208805511
    12540698747158523863050715693290963295227443043557
    66896648950445244523161731856403098711121722383113
    62229893423380308135336276614282806444486645238749
    30358907296290491560440772390713810515859307960866
    70172427121883998797908792274921901699720888093776
    65727333001053367881220235421809751254540594752243
    52584907711670556013604839586446706324415722155397
    53697817977846174064955149290862569321978468622482
    83972241375657056057490261407972968652414535100474
    82166370484403199890008895243450658541227588666881
    16427171479924442928230863465674813919123162824586
    17866458359124566529476545682848912883142607690042
    24219022671055626321111109370544217506941658960408
    07198403850962455444362981230987879927244284909188
    84580156166097919133875499200524063689912560717606
    05886116467109405077541002256983155200055935729725
    71636269561882670428252483600823257530420752963450"""
    series = series.replace("\n    ", "")  # hackish way of reading in easily

    output = 0
    for i in range(1000 - num):
        product = 1
        for y in series[i : i + num]:
            product = product * int(y)
        if product > output:
            output = product
    return output


def problem_nine(num):
    """
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
        a^2 + b^2 = c^2
    For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.
    """
    for a in range(1, num // 2 + 1):
        for b in list(range(a + 1, num)):
            if math.sqrt(a * a + b * b).is_integer():
                c = int(math.sqrt(a * a + b * b))
                if a + b + c == num:

                    return a * b * c


def problem_ten(num: int) -> list:
    """
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million.
    """
    prime_bool = prime.eratosthenes_sieve_prime(num)

    return sum(i for i in range(num) if prime_bool[i])

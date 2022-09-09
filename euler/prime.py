"""Prime number related helper functions"""
import math


def is_prime(num: int) -> bool:
    """function to check if the number
    is prime or not"""
    if num == 0:
        return False
    if num == 1:
        return False
    for i in range(2, int(abs(num) ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_factors(num: int) -> list:
    """
    Assume n is a positive natural number

        returns a list of prime factors of n
    """
    if is_prime(num):
        return [num]
    if num == 1:
        return []

    factors = []
    c = 2
    while num > 1:

        if num % c == 0:
            factors.append(c)
            num = num / c
        else:
            c = c + 1
    return factors


def distinct_prime_factors(num: int) -> set:
    """
    Assume n is a positive natural number

        returns a list of distinct prime factors of n
    """
    factors = set()
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            factors.add(i)
    if num > 1:
        factors.add(num)
    return factors


def eratosthenes_sieve_prime(num):
    """Return all prime numbers up to a given limit num"""
    if num <= 2:
        return []

    prime_bool = [True] * num
    prime_bool[0] = False
    prime_bool[1] = False

    for i in range(2, math.isqrt(num) + 1):
        if prime_bool[i]:
            for x in range(i * i, num, i):
                prime_bool[x] = False
    return prime_bool


def divisors_count(num):
    """
    Returns the count of divisors of {num}: Assumes {num} is a positive natural number
    """
    p_factors = prime_factors(num)
    dict = {i: p_factors.count(i) for i in set(p_factors)}
    divisors = 1
    for v in dict.values():
        divisors = divisors * (v + 1)

    return divisors


def divisors(num: int, proper: bool = True) -> list:
    """
    Returns the proper divisors of {num}: Assumes {num} is a positive natural number

        parameters:
            propers: (default) True = returns only proper divisors, e.g., not including {num} itself
    """
    p_factors = prime_factors(num)
    dict = {i: p_factors.count(i) for i in set(p_factors)}
    divs = [1]
    for k, v in dict.items():
        divs += [x * k**i for i in range(1, v + 1) for x in divs]

    if proper:
        divs.remove(num)

    return sorted(divs)


if __name__ == "__main__":
    for i in range(1, 20):
        print(i, prime_factors(i), divisors(i, True))

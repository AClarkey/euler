"""Prime number related helper functions"""
import math


def is_prime(num: int) -> bool:
    """
    Assume n is a positive natural number

        returns True/False of prime
    """
    if num == 1:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
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

    output = []
    prime_factor = 2

    while True:
        if num == prime_factor:
            output.append(prime_factor)
            break

        while num % prime_factor == 0:
            output.append(prime_factor)
            num = num / prime_factor

        prime_factor += 1

        while is_prime(prime_factor) is False:
            prime_factor += 1

        if prime_factor > num:
            break

    return output


def eratosthenes_sieve(num):
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


def divisors(num):
    """
    Returns the count of divisors of num

        Assume num is a positive natural number
    """
    p_factors = prime_factors(num)
    dict = {i: p_factors.count(i) for i in set(p_factors)}
    divisors = 1
    for i in dict.keys():
        divisors = divisors * (dict[i] + 1)

    return divisors


if __name__ == "__main__":
    for i in range(50):
        print(i, divisors(i))

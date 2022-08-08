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


def prime_factors_old(num: int) -> list:
    """
    Assume n is a positive natural number

        returns a list of prime factors of n
    """
    output = [
        i for i in range(2, int(math.sqrt(num) + 1)) if is_prime(i) and num % i == 0
    ]
    return output


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


if __name__ == "__main__":
    print("two")
    print(prime_factors(2), type(prime_factors(2)))

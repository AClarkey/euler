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
    output = [
        i for i in range(2, int(math.sqrt(num) + 1)) if is_prime(i) and num % i == 0
    ]
    return output


# if __name__ == "__main__":
# two = prime_factors(13195)
# print(two[-1])

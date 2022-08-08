"""Prime number related helper functions"""


def is_prime(n: int) -> bool:
    """
    Assume n is a positive natural number

        returns True/False of prime
    """
    if n == 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def prime_factors(n: int) -> list:
    """
    Assume n is a positive natural number

        returns a list of prime factors of n
    """

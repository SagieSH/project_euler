import math


def decompose_to_primes(num):
    decomposition = dict()
    p = 2
    while num > 1:
        if p * p > num:  # no need to check all the range from p to num
            p = num
        if (num % p) == 0:
            if p not in decomposition.keys():
                decomposition[p] = 0
            decomposition[p] += 1
            num //= p
            p = 2
        else:
            p += 1
    return decomposition


def gcd(a, b):
    if b > a:
        a, b = b, a
    while a % b != 0:
        a, b = b, a % b
    return b


def minimize_fraction(numerator, denominator):
    g = gcd(numerator, denominator)
    return numerator // g, denominator // g


def sum_modulo(it, modulo):
    result = 0
    for x in it:
        result = (result + x) % modulo
    return result


def prod_modulo(it, modulo):
    result = 1
    for x in it:
        result = (result * x) % modulo
    return result


def factorial_modulo(num, mod):
    return prod_modulo(range(1, num + 1), mod)


def calc_modulo(mod):
    def outer(func):
        def inner(*args, **kwargs):
            return func(*args, **kwargs) % mod
        return inner
    return outer


def get_prime_list(limit=None, amount=None, get_non_primes=False):
    if limit is None:
        assert amount is not None, "Must include limit or amount!"
        # This is an upper bound on the {amount}'th prime
        limit = int(amount * (math.log(amount) + 10))
    else:
        amount = limit
    primes = list()
    is_prime = [None] * limit
    is_prime[0], is_prime[1] = False, False

    p = 0
    while len(primes) < amount:
        try:
            p = is_prime.index(None, p)
        except ValueError:
            break
        is_prime[p] = True
        primes.append(p)
        for mul in range(2, math.ceil(limit / p)):
            is_prime[p * mul] = False

    if get_non_primes:
        return is_prime
    return primes

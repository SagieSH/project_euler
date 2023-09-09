
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
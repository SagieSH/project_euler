
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


def minimize_fraction(numerator, denominator):
    min_numerator, min_denominator = numerator, denominator
    numerator_primes = decompose_to_primes(numerator)
    for prime, power in numerator_primes.items():
        for i in range(power):
            if min_denominator % prime == 0:
                min_denominator //= prime
    min_numerator //= (denominator // min_denominator)
    return min_numerator, min_denominator

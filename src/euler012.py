
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


def triangle_number(num):
    return (num * (num + 1)) // 2


def divisor_amount(num):
    decomposition = decompose_to_primes(num)
    result = 1
    for power in decomposition.values():
        result *= (power + 1)
    return result


k = 1
while (d := (divisor_amount(next_triangle_number := triangle_number(k)))) <= 500:
    print(k, next_triangle_number, d)
    k += 1

# The answer is 76576500
print(k, next_triangle_number, d)

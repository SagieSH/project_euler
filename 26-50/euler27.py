LIMIT = 100000
PRIMES = []
NON_PRIMES = set()


def fill_primes():
    global PRIMES, NON_PRIMES

    n = 2
    m = 2
    while n < LIMIT:
        print(n)
        PRIMES.append(n)
        while n * m < LIMIT:
            NON_PRIMES.add(n * m)
            m += 1
        m = 2
        n += 1
        while n in NON_PRIMES:
            n += 1


def calc_poly(a, b, n):
    return (n * n) + (a * n) + b


max_consecutive = 0
max_a, max_b = 1, 1
fill_primes()
for b in PRIMES:
    if b > 1000:
        break
    for a in range(-999, 1000, 2):
        print(a, b, PRIMES.index(b))
        n = 0
        while calc_poly(a, b, n) in PRIMES:
            n += 1
        if n > max_consecutive:
            max_consecutive = n - 1
            max_a, max_b = a, b

print(f"the polynomial: n^2 + {max_a}n + {max_b}")
print(f"produces primes, for 0 <= n <= {max_consecutive}")

# The answer is -59231
print(f"coefficient product is: {max_a * max_b}")

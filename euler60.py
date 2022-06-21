
LIMIT = 1000
PRIMES = []


# def is_prime(n):
#     i = 2
#     while i * i <= n:
#         if n % i == 0:
#             return False
#         i += 1
#     return True


def fill_primes():
    non_primes = set()
    n = 2
    m = 2

    while n < LIMIT:
        PRIMES.append(n)
        while n * m < LIMIT:
            non_primes.add(n * m)
            m += 1
        m = 2
        n += 1
        while n in non_primes:
            n += 1

    print('finished primes:', len(PRIMES))

if __name__ == '__main__':
    fill_primes()

    for i1 in range(len(PRIMES)):
        for i2 in range(i1, len(PRIMES)):
            for i3 in range(i2, len(PRIMES)):
                for i4 in range(i3, len(PRIMES)):
                    for i5 in range(i4, len(PRIMES)):
                        x = PRIMES[i1] + PRIMES[i2] + PRIMES[i3] + PRIMES[i4] + PRIMES[i5]

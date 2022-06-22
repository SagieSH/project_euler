
LIMIT = 2000000
PRIMES = []

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

# The answer is 142913828922
print(sum(PRIMES))


def is_prime(n):
    k = 2
    while k * k <= n:
        if (n % k) == 0:
            return False
        k += 1
    return True


primes = []
p = 2
while len(primes) < 10001:
    if is_prime(p):
        primes.append(p)
    p += 1

# The answer is 104743
print(primes[-1])

def find_largest_prime_divisor(n):
    p = 2
    while p < n:
        if (n % p) == 0:
            n //= p
            p = 2
        else:
            p += 1
    return n


# The answer is 6857
print(find_largest_prime_divisor(600851475143))

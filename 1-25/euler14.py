
MEMORY_COLLATZ = {1: 1}


def memoize_collatz(func):
    def inner(num):
        if num not in MEMORY_COLLATZ.keys():
            MEMORY_COLLATZ[num] = func(num)
        return MEMORY_COLLATZ[num]

    return inner


@memoize_collatz
def collatz(num):
    if num % 2 == 0:
        return 1 + collatz(num // 2)
    return 1 + collatz((3 * num) + 1)


max_collatz = 1
max_num = 1
for n in range(1, 1000000):
    curr = collatz(n)
    if curr > max_collatz:
        max_num = n
        max_collatz = curr

# The answer is 837799
print(max_num, max_collatz)

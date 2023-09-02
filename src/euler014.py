
from functools import cache


@cache
def collatz(num):
    if num == 1:
        return 1
    if num % 2 == 0:
        return 1 + collatz(num // 2)
    return 1 + collatz((3 * num) + 1)


max_collatz = 1
max_num = 1
for n in range(1, 1000000):
    print(n)
    curr = collatz(n)
    if curr > max_collatz:
        max_num = n
        max_collatz = curr

# The answer is 837799
print(max_num, max_collatz)

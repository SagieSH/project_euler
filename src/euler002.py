
from functools import lru_cache


@lru_cache
def fib(num):
    if (num == 0) or (num == 1):
        return num
    return fib(num - 1) + fib(num - 2)


n = 1
result = 0
while (next_fib := fib(n)) <= 4000000:
    if next_fib % 2 == 0:
        result += next_fib
    n += 1

# The answer is 4613732
print(result)

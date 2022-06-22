
MEMORY_FIB = {1: 1, 2: 2}


def memoize_fib(func):
    def inner(num):
        if num not in MEMORY_FIB.keys():
            MEMORY_FIB[num] = func(num)
        return MEMORY_FIB[num]

    return inner


@memoize_fib
def fib(num):
    return fib(num - 1) + fib(num - 2)


n = 1
result = 0
while (next_fib := fib(n)) <= 4000000:
    if next_fib % 2 == 0:
        result += next_fib
    n += 1

# The answer is 4613732
print(result)

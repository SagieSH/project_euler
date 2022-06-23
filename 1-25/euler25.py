from functools import cache


@cache
def fib(num):
    if (num == 0) or (num == 1):
        return num
    return fib(num - 1) + fib(num - 2)


result = 0
while len(str(fib(result))) < 1000:
    result += 1

# The answer is 4782
print(result)

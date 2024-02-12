
from time import time

MAX_NUMBER = 28124


def divisor_sum(num):
    result = 0
    for k in range(1, num // 2 + 1):
        if num % k == 0:
            result += k
    return result


def is_abundant(num):
    return divisor_sum(num) > num


time1 = time()
abundant = list()
for number in range(1, MAX_NUMBER):
    print(number)
    if is_abundant(number):
        abundant.append(number)
time2 = time()
sums = set()
for index, num1 in enumerate(abundant[:-1]):
    for num2 in abundant[index:]:
        if (num1 + num2) >= MAX_NUMBER:
            break
        print(num1, num2)
        sums.add(num1 + num2)
time3 = time()
result = 0
for num in range(1, MAX_NUMBER):
    print(num)
    if num not in sums:
        result += num
time4 = time()

print(f"find all abundant: {time2 - time1}")
print(f"find all two sums: {time3 - time2}")
print(f"find all not a sum: {time4 - time3}")
print(f"overall time: {time4 - time1}")

# The answer is 4179871
print(f"result: {result}")

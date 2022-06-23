
from functools import cache


@cache
def divisor_sum(num):
    result = 0
    for k in range(1, num // 2 + 1):
        if num % k == 0:
            result += k
    return result


def is_amicable(num):
    d_num = divisor_sum(num)
    return (num != d_num) and (num == divisor_sum(d_num))


# The answer is 31626
print(sum(number for number in range(1, 10000) if is_amicable(number)))

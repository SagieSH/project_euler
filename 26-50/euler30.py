from functools import reduce


def sum_of_powered_digits(num, power):
    return sum(map((lambda c: (int(c) ** power)), str(num)))


# The answer is 443839
print(sum([num for num in range(10, 1000000) if (num == sum_of_powered_digits(num, 5))]))

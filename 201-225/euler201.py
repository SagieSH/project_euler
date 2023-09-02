"""
What I wanna do here, is create the following dict:
    Key: Number between 0 and sum([x ** 2 for x in range(1, 101)]) standing for different sums.
    Value: The following dict:
        Key: Number between 0 and 100 standing for the amount of numbers in the sum
        Value: The number of possibilities to create The original key,
                using the amount of number in the sum as specified in the key.
This dict can be created dynamically.
"""
from collections import defaultdict
from copy import deepcopy
import time

options_dict = dict()


def constant_factory(value):
    return lambda: value


def print_dict(d):
    for key, value in d.items():
        print(f"{key}:")
        for key2, value2 in value.items():
            print(f"\t{key2}: {value2}")


def initialize_dict():
    global options_dict
    options_dict = defaultdict(lambda: (defaultdict(constant_factory(0))))
    options_dict[0][0] = 1


def add_num(num):
    global options_dict
    old_dict = deepcopy(options_dict)
    for sum_option, inner_dict in old_dict.items():
        for operand_amount, option_amount in inner_dict.items():
            if operand_amount < 50:
                options_dict[sum_option + num][operand_amount + 1] += option_amount


def main():
    initialize_dict()
    final_sum = 0
    overall_start = time.time()
    for num in range(1, 101):
        print(num, end="")
        start = time.time()
        add_num(num ** 2)
        end = time.time()
        print(f": {end - start}")
    overall_end = time.time()
    print(f"overall time: {overall_end - overall_start}")
    for key, d in options_dict.items():
        if d[50] == 1:
            final_sum += key

    # The answer is: 115039000
    print(f"final_sum: {final_sum}")


if __name__ == '__main__':
    main()

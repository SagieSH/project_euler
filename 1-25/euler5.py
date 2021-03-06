
from functools import reduce


def decompose_to_primes(num):
    decomposition = dict()
    p = 2
    while num > 1:
        if p * p > num:  # no need to check all the range from p to num
            p = num
        if (num % p) == 0:
            if p not in decomposition.keys():
                decomposition[p] = 0
            decomposition[p] += 1
            num //= p
            p = 2
        else:
            p += 1
    return decomposition


def two_dict_max(dict1, dict2):
    max_dict = dict()
    for key1 in dict1.keys():
        if key1 not in dict2.keys():
            max_dict[key1] = dict1[key1]
        else:
            max_dict[key1] = max(dict1[key1], dict2[key1])

    for key2 in dict2.keys():
        if key2 not in max_dict.keys():
            max_dict[key2] = dict2[key2]

    return max_dict


def dict_to_num(d):
    return reduce((lambda a, b: a * b), [prime ** power for prime, power in d.items()])


max_num_dict = dict()
for n in range(1, 21):
    max_num_dict = two_dict_max(max_num_dict, decompose_to_primes(n))

# The answer is 232792560
print(dict_to_num(max_num_dict))

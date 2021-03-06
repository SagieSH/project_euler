
from functools import cache


@cache
def lattice_paths_1(length, depth):
    if min(length, depth) == 0:
        return 1

    return lattice_paths_1(length - 1, depth) + lattice_paths_1(length, depth - 1)


def lattice_paths_2(length, depth):
    numerator = 1
    for ii in range(length + 1, length + depth + 1):
        numerator *= ii
    denominator = 1
    for ii in range(1, depth + 1):
        denominator *= ii

    return numerator // denominator


def lattice_paths(length, depth):
    print(f"For length: {length}, depth: {depth}. 1:", lattice_paths_1(length, depth))
    print(f"For length: {length}, depth: {depth}. 2:", lattice_paths_2(length, depth))


# The answer is 137846528820
lattice_paths(20, 20)


from functools import lru_cache

NUMBERS_PATH = "euler18_pyramid.txt"
ROWS = 15
PYRAMID = []


def parse_pyramid():
    global PYRAMID

    with open(NUMBERS_PATH, 'r') as numbers_file:
        for line in numbers_file.readlines():
            if line[-1] == '\n':
                line = line[:-1]
            PYRAMID.append([int(num) for num in line.split()])
    return PYRAMID


@lru_cache
def find_max_path(row, index):
    my_val = PYRAMID[row][index]
    if row == ROWS - 1:
        return my_val
    return my_val + max(find_max_path(row + 1, index), find_max_path(row + 1, index + 1))


parse_pyramid()
# The answer is 1074
print(find_max_path(0, 0))

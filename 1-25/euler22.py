
from functools import reduce

PATH_NAMES = "euler22_names.txt"
NAMES = list()


def parse_names():
    global NAMES

    with open(PATH_NAMES, 'r') as names_file:
        NAMES = names_file.readline().split('","')
        NAMES[0] = NAMES[0][1:]
        NAMES[-1] = NAMES[-1][:-1]
    NAMES.sort()


def alphabetical_value(name):
    normalizer = ord('A') - 1
    return sum(map((lambda a: ord(a) - normalizer), name))


parse_names()
values = map(alphabetical_value, NAMES)

# The answer is 871198282
print(sum((index + 1) * value for index, value in enumerate(values)))

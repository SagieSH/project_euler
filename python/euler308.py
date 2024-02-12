FRACTION_LIST = [
    (17, 91),
    (78, 85),
    (19, 51),
    (23, 38),
    (29, 33),
    (77, 29),
    (95, 23),
    (77, 19),
    (1, 17),
    (11, 13),
    (13, 11),
    (15, 2),
    (1, 7),
    (55, 1)
]


def fraction_generator(index):
    while True:
        while index < len(FRACTION_LIST):
            yield FRACTION_LIST[index]
            index += 1
        index = 0


def fractranator(seed):
    current_number = seed
    yield current_number
    while True:
        for frac in FRACTION_LIST:
            if ((current_number * frac[0]) % frac[1]) == 0:
                current_number = ((current_number * frac[0]) // frac[1])
                yield current_number
                break

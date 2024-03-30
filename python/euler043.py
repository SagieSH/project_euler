import itertools


def is_special(num: int):
    num234 = int(str(num)[1:4])
    if num234 % 2 != 0:
        return False

    num345 = int(str(num)[2:5])
    if num345 % 3 != 0:
        return False
    
    num456 = int(str(num)[3:6])
    if num456 % 5 != 0:
        return False
    
    num567 = int(str(num)[4:7])
    if num567 % 7 != 0:
        return False
    
    num678 = int(str(num)[5:8])
    if num678 % 11 != 0:
        return False
    
    num789 = int(str(num)[6:9])
    if num789 % 13 != 0:
        return False
    
    num8910 = int(str(num)[7:10])
    if num8910 % 17 != 0:
        return False

    return True


def main():
    specials = []
    pandigitals = itertools.permutations(range(10))
    for perm in pandigitals:
        if perm[0] == 0:
            continue
        num = int("".join(str(x) for x in perm))
        if is_special(num):
            specials.append(num)
    
    # The answer is: 16695334890
    print(sum(specials))


if __name__ == '__main__':
    main()

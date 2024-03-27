
def is_pandigital(num):
    s = str(num)
    if len(s) != 9:
        return False

    for digit in range(1, 10):
        if str(digit) not in s:
            return False

    return True


def concatenated_product(num, max_digit):
    result = ""
    for digit in range(1, max_digit + 1):
        result += str(num * digit)
    return int(result)


def main():
    max_pandigital = 0
    for num in range(1, 10000):
        for max_digit in range(2, 10):
            x = concatenated_product(num, max_digit)
            if is_pandigital(x) and x > max_pandigital:
                max_pandigital = x
    
    
    # The answer is 932718654
    print(max_pandigital)


if __name__ == '__main__':
    main()

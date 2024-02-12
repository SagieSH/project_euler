
def is_palindrome(s):
    return s == s[::-1]


def main():
    double_palindromes = list()
    for num in range(1000000):
        if is_palindrome(str(num)) and is_palindrome(bin(num)[2:]):
            double_palindromes.append(num)

    # The answer is 872187
    print(sum(double_palindromes))


if __name__ == '__main__':
    main()

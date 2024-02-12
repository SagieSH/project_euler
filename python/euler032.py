
"""
Need to seperate into different sections.
1. When the first number is of length 1:
    In that case, the second number must be of 4 digits:
    a. If the second number is 3 digits, then the product is at most 4 digits, and overall not enough digits.
    b. If the second number is 5 digits, then the product is at least 5 digits, and overall too many digits.
2. When the first number is of length 2:
    In that case, the second number must be of 3 digits:
    a. If the second number is 2 digits, then the product is at most 4 digits, and overall not enough digits.
    b. If the second number is 4 digits, then the product is at least 5 digits, and overall too many digits.
And these are all possible options.
"""

DIGITS = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def is_pandigital_str(nums_str):
    if len(nums_str) != 9:
        return False
    digits = [False] * 9
    for c in nums_str:
        digit = int(c)
        if digit == 0:
            return False
        digits[digit - 1] = True
    return False not in digits


def is_pandigital_product(num1_str, num2_str):
    product = int(num1_str)*int(num2_str)
    if is_pandigital_str(num1_str + num2_str + str(product)):
        return product


def find_all_pandigidal_products():
    pandigital_products = set()
    for d1 in DIGITS:
        for d2 in DIGITS:
            for d3 in DIGITS:
                for d4 in DIGITS:
                    for d5 in DIGITS:
                        product = is_pandigital_product(d1, d2 + d3 + d4 + d5)
                        if product is not None:
                            print(f"{d1} x {d2 + d3 + d4 + d5} = {product}")
                            pandigital_products.add(product)
                        product = is_pandigital_product(d1 + d2, d3 + d4 + d5)
                        if product is not None:
                            print(f"{d1 + d2} x {d3 + d4 + d5} = {product}")
                            pandigital_products.add(product)
    return pandigital_products


def main():
    products = list(find_all_pandigidal_products())
    print(products)
    print(sum(products))


# The answer is 45228
if __name__ == '__main__':
    main()

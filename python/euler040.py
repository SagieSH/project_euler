
import math


def find_nth_digit_of_champernowne_constant(n):
    """
    Find the nth digit of the Champernowne constant.
    
    The Champernowne constant is formed by concatenating the positive integers:
    0.123456789101112131415161718192021...
    
    :param n: The position of the digit to find (1-indexed).
    :return: The nth digit of the Champernowne constant.
    """
    current_number = 1
    digit_amount = 0
    
    while digit_amount < n:
        # Calculate the number of digits in the current number
        digits_in_current_number = len(str(current_number))

        # Check if adding this number's digits exceeds n
        if digit_amount + digits_in_current_number >= n:
            # Find the exact digit we need
            return int(str(current_number)[n - digit_amount - 1])

        # Update the digit amount and move to the next number
        digit_amount += digits_in_current_number
        current_number += 1


def main():
    """
    Main function to solve the problem described in Project Euler 040.
    """
    # The answer is 210
    print(
        math.prod(
            [find_nth_digit_of_champernowne_constant(n) for n in [1, 10, 100, 1000, 10000, 100000, 1000000]]
        )
    )

if __name__ == "__main__":
    main()
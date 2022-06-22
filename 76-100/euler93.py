from typing import List, Tuple
from itertools import permutations
import time


def create_parentheses_list():
    return [
        [(0, 2), (0, 3)],
        [(0, 2), (2, 4)],
        [(0, 3), (1, 3)],
        [(1, 3), (1, 4)],
        [(1, 4), (2, 4)]
    ]


def is_positive_integer(num):
    return (num == int(num)) and num > 0


def all_expressions(a, b, c, d, parentheses):
    results = set()
    operations = ['+', '-', '*', '/']
    for perm in permutations([a, b, c, d]):
        for op1, op2, op3 in [(i, j, k) for i in operations for j in operations for k in operations]:
            for paren_list in parentheses:
                expression = f"{perm[0]}{op1}{perm[1]}{op2}{perm[2]}{op3}{perm[3]}"
                for paren in paren_list:
                    first_location = expression.find(str(perm[paren[0]]))
                    second_location = expression.find(str(perm[paren[1] - 1])) + 1
                    expression = expression[:first_location] + '(' + expression[first_location:second_location] \
                                 + ')' + expression[second_location:]
                try:
                    result = eval(expression)
                except ZeroDivisionError:
                    continue
                if is_positive_integer(result):
                    results.add(result)
    return results


def find_longest_streak(numbers):
    for index, num in enumerate(numbers):
        if index != (num - 1):
            return index


parentheses_list: List[List[Tuple[int, int]]]  # List of all the ways you can put parentheses in an expression
parentheses_list = create_parentheses_list()
all_digit_tuples = [(a, b, c, d) for a in range(1, 10) for b in range(a + 1, 10)
                    for c in range(b + 1, 10) for d in range(c + 1, 10)]
max_streak = 0
max_abcd = ""
initial_time = time.time()
for a, b, c, d in all_digit_tuples:
    print(a, b, c, d)
    all_results = all_expressions(a, b, c, d, parentheses_list)
    curr_streak = find_longest_streak(all_results)
    if curr_streak > max_streak:
        max_streak = curr_streak
        max_abcd = f"{a}{b}{c}{d}"
final_time = time.time()

# The answer is 1258
print(f"abcd: {max_abcd}, streak: {max_streak}, time: {final_time - initial_time}")

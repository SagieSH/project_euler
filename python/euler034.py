from math import factorial
from itertools import combinations

FACTS = {str(x): factorial(x) for x in range(10)}
MAX_LEN = 7


def is_facts_sum(num):
    facts_sum = 0
    for digit in str(num):
        facts_sum += FACTS[digit]
    return (facts_sum == num)


def main():
    combs = list()
    for num in range(10, 10 ** MAX_LEN):
        if is_facts_sum(num):
            combs.append(num)
    
    # The answer is: 40730
    print(sum(combs))


if __name__ == '__main__':
    main()

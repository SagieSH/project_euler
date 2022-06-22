
from typing import List, Dict, Tuple

piles_memory: Dict[int, int] = {0: 1}


def pentagonal(k):
    return (k * ((3 * k) - 1)) / 2


def all_partitions(coins: int) -> int:
    """
    :param coins: overall coins we need to find the partition of to piles
    :return: amount of ways we can divide to piles
    """
    global piles_memory

    if coins < 0:
        return 0

    if coins not in piles_memory.keys():
        k = 0
        next_partition_number = 1
        result = 0
        while next_partition_number > 0:
            k += 1
            for ii in [1, -1]:
                next_pentagonal = pentagonal(ii * k)
                next_partition_number = all_partitions(coins - next_pentagonal)
                result += ((-1) ** (k + 1)) * next_partition_number
        piles_memory[coins] = result % 1000000

    return piles_memory[coins]


def main():
    n = 1
    # amount = all_partitions(n)
    amount = 1
    while amount != 0:
        print(f"n: {n}, partitions: {amount}")
        n += 1
        amount = all_partitions(n)

    # The answer is n = 55374
    print(f"n: {n}, partitions: {amount}")


if __name__ == '__main__':
    main()


from typing import List, Dict, Tuple

piles_memory: Dict[int, List[Tuple[int, int]]] = dict()


def all_partitions(coins: int, limit: int) -> List[Tuple[int, int]]:
    """
    :param coins: overall coins we need to find the partition of to piles
    :param limit: cannot have a pile with more coins than limit
    :return: each tuple in the list is of the format: [first pile, amount of piles with that first pile]
    """
    global piles_memory

    if (coins == 0) or (limit == 0):
        return [(0, 1)]
    if (coins < 1) or (limit < 1) or (limit > coins):
        return []
    if limit == 1:
        return [(1, 1)]

    if coins not in piles_memory.keys():
        partitions = [(1, 1)]
        for first_pile in range(2, coins + 1):
            previous_index = first_pile - 2
            next_partitions = all_partitions(coins - first_pile, min(first_pile, coins - first_pile))
            partitions.append((first_pile, next_partitions[-1][1] + partitions[previous_index][-1]))
        piles_memory[coins] = partitions

    no_limit_partitions = piles_memory[coins]
    return [partition for partition in no_limit_partitions if (partition[0] <= limit)]


def main():
    n = 2
    # partitions = all_partitions(n, n)
    partitions = [[]]
    amount = 1
    while n != 6:
        print(f"n: {n}, partitions: {amount}")
        n += 1
        partitions = all_partitions(n, n)
        amount = partitions[-1][1]

    print(f"amount: {partitions[-1][1]}")
    print(partitions)


if __name__ == '__main__':
    main()

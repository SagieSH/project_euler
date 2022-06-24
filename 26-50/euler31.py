from typing import List, Tuple, Dict

POSSIBLE_COINS = [1, 2, 5, 10, 20, 50, 100, 200]
coins_memory: Dict[int, List[Tuple[int, int]]] = dict()


def all_coin_splits(amount, limit):
    global coins_memory

    if (amount < 0) or (limit < 0):
        return []
    if (amount == 0) or (limit == 0):
        return [(0, 1)]
    if limit == 1:
        return [(1, 1)]

    if amount not in coins_memory.keys():
        partitions = [(1, 1)]
        for index, first_coin in enumerate(POSSIBLE_COINS[1:]):
            if first_coin > amount:
                break
            next_partitions = all_coin_splits(amount - first_coin, first_coin)
            # print(index, first_coin, partitions, next_partitions)
            partitions.append((first_coin, next_partitions[-1][1] + partitions[index][1]))
        coins_memory[amount] = partitions

    no_limit_partitions = coins_memory[amount]
    return [partition for partition in no_limit_partitions if (partition[0] <= limit)]


partitions = all_coin_splits(200, 200)

# The answer is 73682
print(partitions[-1][1])

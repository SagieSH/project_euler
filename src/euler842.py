from functools import lru_cache

MODULO = (10 ** 9) + 7


@lru_cache
def block_placement(block_amount, row_len):
    # Can be improved by multiplying with factorial
    if (row_len == 0) or (row_len == 1):
        return 0
    if block_amount == 1:
        return row_len - 1
    return sum(
        [(block_placement(block_amount - 1, index) + block_placement(block_amount - 1, row_len - index - 2)) for index
         in range(row_len - 1)]) % MODULO


def num_of_graphs_containing(vertex_amount, edge_amount):
    return (2 ** (edge_amount - 1)) * block_placement(edge_amount - 1, vertex_amount - 2) *

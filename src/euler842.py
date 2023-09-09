from functools import lru_cache
from utils.number_theory import calc_modulo, factorial_modulo, prod_modulo

MODULO = (10 ** 9) + 7


@lru_cache
@calc_modulo(MODULO)
def unordered_block_placement(block_amount, row_len):
    # Can be improved by multiplying with factorial
    # if :
    #     raise ValueError("bad usage of block_placement")
    if (row_len < 0) or (block_amount < 0) or (row_len < (2 * block_amount)):
        return 0
    if row_len == (2 * block_amount):
        return 1
    return unordered_block_placement(block_amount, row_len - 1) + unordered_block_placement(block_amount - 1, row_len - 2)


@lru_cache
@calc_modulo(MODULO)
def block_placement(block_amount, row_len):
    return factorial_modulo(block_amount, MODULO) * unordered_block_placement(block_amount, row_len)


@lru_cache
@calc_modulo(MODULO)
def num_of_graphs_containing(vertex_amount, edge_amount):
    """
    This returns the number of graphs with {vertex_amount} vertices, which are a hamiltonian path on them,
    and in addition, this path must contain {edge_amount} of disjoint edges.
    """
    return prod_modulo(
        [2] * (edge_amount - 1),
        MODULO
    ) * block_placement(
        edge_amount - 1,
        vertex_amount - 2
    ) * factorial_modulo(
        vertex_amount - (2 * edge_amount),
        MODULO
    )


@lru_cache
@calc_modulo(MODULO)
def num_of_graphs_containing_with_crossing(vertex_amount, edge_amount):
    """
    This returns the number of graphs with {vertex_amount} vertices, which are a hamiltonian path on them,
    and in addition, this path must contain at least two of {edge_amount} (which means there will be a crossing).
    (n choose 2) graphs with intersection of 2
    (n choose 3) graphs with intersection of 3, we counted them (3 choose 2) times in the first part.
    (n choose 4) graphs with intersection of 4, we counted them (4 choose 2) times in the first part, 
                    and (4 choose 3) in the second part.
    """


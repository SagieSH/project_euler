from functools import lru_cache
from math import comb
import cmath
import time
from itertools import combinations
from utils.number_theory import calc_modulo, factorial_modulo, prod_modulo, sum_modulo
from utils.drawing import plot_complex_points, set_limits, make_square

MODULO = (10 ** 9) + 7
CLOSENESS = 1e-9
ROUND_SIZE = 9


@lru_cache
@calc_modulo(MODULO)
def unordered_block_placement(block_amount, row_len):
    """
    This returns the amount of ways to place {block_amount} identical blocks, inside a row of length {row_len}.
    """
    if (row_len < 0) or (block_amount < 0) or (row_len < (2 * block_amount)):
        return 0
    if row_len == (2 * block_amount):
        return 1
    return unordered_block_placement(block_amount, row_len - 1) + unordered_block_placement(block_amount - 1, row_len - 2)


@lru_cache
@calc_modulo(MODULO)
def block_placement(block_amount, row_len):
    """
    This returns the amount of ways to place {block_amount} unique blocks, inside a row of length {row_len}.
    """
    return factorial_modulo(block_amount, MODULO) * unordered_block_placement(block_amount, row_len)


@lru_cache
@calc_modulo(MODULO)
def num_of_graphs_containing(vertex_amount, edge_amount):
    """
    This returns the number of graphs with {vertex_amount} vertices, which are a hamiltonian path on them,
    and in addition, this path must contain {edge_amount} of disjoint edges.
    Can be done way more efficiently with better combinatorics, however doesn't change the end result.
    """
    return (prod_modulo(
        [2] * (edge_amount - 1),
        MODULO
    ) * block_placement(
        edge_amount - 1,
        vertex_amount - 2
    ) * factorial_modulo(
        vertex_amount - (2 * edge_amount),
        MODULO
    ) % MODULO)


@lru_cache
@calc_modulo(MODULO)
def num_of_graphs_containing_with_crossing(vertex_amount, edge_amount):
    """
    This returns the number of graphs with {vertex_amount} vertices, which are a hamiltonian path on them,
    and in addition, this path must contain at least two of {edge_amount} (which means there will be a crossing).
    """
    if edge_amount < 2:
        return 0
    sum_params = [None, None, 1]
    for i in range(3, edge_amount + 1):
        sum_params.append(1 - sum([(comb(i, j) * sum_params[j]) for j in range(2, i)]))
    return sum([(comb(edge_amount, i) * num_of_graphs_containing(vertex_amount, i) * sum_params[i]) for i in range(2, edge_amount + 1)])


def is_close(x, y):
    return cmath.isclose(x, y, rel_tol=0, abs_tol=CLOSENESS)


def round_complex(p):
    return round(p.real, ROUND_SIZE) + 1j * round(p.imag, ROUND_SIZE)


def initialize_points(n):
    return [cmath.exp((2*cmath.pi*1j) * (k / n)) for k in range(n)]


def four_point_intersection(p1, p2, p3, p4):
    """
    This assumes all points are complex numbers, and that the line (p1, p3) intersects with (p2, p4).
    :return: The intersection point.
    """
    x1, y1 = p1.real, p1.imag
    x2, y2 = p2.real, p2.imag
    x3, y3 = p3.real, p3.imag
    x4, y4 = p4.real, p4.imag
    if is_close(x1, x3):
        grad24 = (y4 - y2) / (x4 - x2)
        return x1 + ((y2 + (grad24 * (x1 - x2))) * 1j)
    else:
        grad13 = (y3 - y1) / (x3 - x1)
    if is_close(x2, x4):
        grad13 = (y3 - y1) / (x3 - x1)
        return x2 + ((y1 + (grad13 * (x2 - x1))) * 1j)
    else:
        grad24 = (y4 - y2) / (x4 - x2)

    x = (y2 - y1 + (x1 * grad13) - (x2 * grad24)) / (grad13 - grad24)
    y13 = y1 + (grad13 * (x - x1))
    y24 = y2 + (grad24 * (x - x2))
    if not is_close(y13, y24):
        raise ValueError(f"Two different values received for {p1}, {p2}, {p3}, {p4}:\n{y13} and {y24}")
    return x + (y13 * 1j)


def get_crossing_dict(points):
    """
    Returns a dict, with each key being an optional crossing point,
        and values being the set of all edges going through said point.
    """
    crossing_point_to_edges = dict()
    for four_point_tuple in combinations(points, 4):
        crossing_point = round_complex(four_point_intersection(*four_point_tuple))
        crossing_point_to_edges[crossing_point] = crossing_point_to_edges.get(crossing_point, set())    
        crossing_point_to_edges[crossing_point].add((four_point_tuple[0], four_point_tuple[2]))
        crossing_point_to_edges[crossing_point].add((four_point_tuple[1], four_point_tuple[3]))
    return crossing_point_to_edges


def main():
    """
    Calculate the amount of crossing points over all hamiltonian paths by summing according to 
        crossing point instead of according to graph.
    """
    overall_start = time.time()
    sums = []
    plot = False
    vertices_options = range(3, 61)
    for vertices in vertices_options:
        start = time.time()
        print(f"Calculating for {vertices}", end=": ")
        points = initialize_points(vertices)
        d = get_crossing_dict(points)
        if plot:
            set_limits((-1, 1), (-1, 1))
            make_square()
            plot_complex_points(points + list(d.keys()), show=True)
        sums.append(sum_modulo([num_of_graphs_containing_with_crossing(vertices, len(d[k])) for k in d.keys()], MODULO))
        end = time.time()
        print(end - start)
    overall_end = time.time()
    
    print(f"Overall time: {overall_end - overall_start}")
    # Answer is: 885226002
    print(f"Result: {sum_modulo(sums, MODULO)}")


if __name__ == '__main__':
    main()

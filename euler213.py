
import numpy as np
import scipy.sparse as sp
from typing import List

SIZE = 30


def coordinate_switch(coordinates):
    # if type(coordinates) is tuple:
    return (coordinates[0] * SIZE) + coordinates[1]

    # assert type(coordinates) is int
    # first = coordinates // SIZE
    # second = coordinates % SIZE
    # return first, second


def calc_potential_hops(row, col):
    return [(row + i, col) for i in [-1, 1] if (0 <= (row + i) < SIZE)] + \
           [(row, col + i) for i in [-1, 1] if (0 <= (col + i) < SIZE)]


def initialize_fleas():
    row_arr: List[int] = []
    col_arr: List[int] = []
    data_arr: List[float] = []
    for row in range(SIZE):
        for col in range(SIZE):
            potentials = calc_potential_hops(row, col)
            for target_row, target_col in potentials:
                row_arr.append(coordinate_switch((row, col)))
                col_arr.append(coordinate_switch((target_row, target_col)))
                data_arr.append(1 / len(potentials))

    position_matrix = sp.coo_matrix((data_arr, (row_arr, col_arr)), shape=(900, 900))
    return position_matrix


def main():
    position_matrix = initialize_fleas()
    e = []
    for ii in range(900):
        e.append(np.zeros(900))
        e[ii][ii] = 1
        for _ in range(50):
            e[ii] = e[ii] * position_matrix
    final_probabilities = []
    for cube in range(900):
        result = 1
        for initial_location in range(900):
            result *= (1 - e[initial_location][cube])
        final_probabilities.append(result)

    # The answer is 330.721154
    print(sum(final_probabilities))


if __name__ == '__main__':
    main()

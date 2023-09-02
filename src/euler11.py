
GRID_PATH = "euler11_grid.txt"
SIZE = 20


def parse_grid():
    grid = []
    with open(GRID_PATH, 'r') as grid_file:
        for line in grid_file.readlines():
            if line[-1] == "\n":
                line = line[:-1]
            grid.append([int(num) for num in line.split(' ')])
    return grid


def find_best_four_prod(grid):
    max_prod = 0

    # find maximum along the lines
    for first in range(SIZE):
        for second in range(SIZE - 4):
            horizontal_prod = 1
            vertical_prod = 1
            for i in range(4):
                horizontal_prod *= grid[first][second + i]
                vertical_prod *= grid[second + i][first]
            prod = max(horizontal_prod, vertical_prod)
            if prod > max_prod:
                max_prod = prod

    # find maximum along diagonals
    for first in range(SIZE - 4):
        for second in range(SIZE - 4):
            left_to_right_prod = 1
            right_to_left_prod = 1
            for i in range(4):
                left_to_right_prod *= grid[first + i][second + i]
                right_to_left_prod *= grid[SIZE - 1 - first - i][second + i]
            prod = max(left_to_right_prod, right_to_left_prod)
            if prod > max_prod:
                max_prod = prod

    return max_prod


# The answer is 70600674
print(find_best_four_prod(parse_grid()))

from math import sqrt


def find_perimeter_of_right_triangle(side1, side2):
    return side1 + side2 + sqrt((side1 * side1) + (side2 * side2))


def main():
    # This list represents how many solutions there are for each perimeter
    perimeters = [0] * 1001

    for side1 in range(1, 1000):
        for side2 in range(1, 1000):
            p = find_perimeter_of_right_triangle(side1, side2)
            if p <= 1000 and (int(p) == p):
                perimeters[int(p)] += 1
    
    # The answer is 840
    print(perimeters.index(max(perimeters)))


if __name__ == '__main__':
    main()

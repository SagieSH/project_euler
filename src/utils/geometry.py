import math
import cmath


def four_point_intersection(p1, p2, p3, p4):
    """
    This assumes all points are complex numbers, and that the line (p1, p3) intersects with (p2, p4).
    :return: The intersection point.
    """
    x1, y1 = p1.real, p1.imag
    x2, y2 = p2.real, p2.imag
    x3, y3 = p3.real, p3.imag
    x4, y4 = p4.real, p4.imag
    try:
        grad13 = (y3 - y1) / (x3 - x1)
    except ZeroDivisionError:
        grad24 = (y4 - y2) / (x4 - x2)
        return x1 + ((y2 + (grad24 * (x1 - x2))) * 1j)
    try:
        grad24 = (y4 - y2) / (x4 - x2)
    except ZeroDivisionError:
        grad13 = (y3 - y1) / (x3 - x1)
        return x2 + ((y1 + (grad13 * (x2 - x1))) * 1j)

    x = (y2 - y1 + (x1 * grad13) - (x2 * grad24)) / (grad13 - grad24)
    y13 = y1 + (grad13 * (x - x1))
    y24 = y2 + (grad24 * (x - x2))
    assert abs(y13 - y24) < (10 ** -9)
    return x + (y13 * 1j)

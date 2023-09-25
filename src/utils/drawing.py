import matplotlib.pyplot as plt
import numpy as np

EPSILON = 1e-2


def set_limits(xlims, ylims):
    plt.xlim(*xlims)
    plt.ylim(*ylims)


def make_square():
    ax = plt.gca()
    ax.set_aspect(1)


def complex_points_to_coords(points):
    x_values = [p.real for p in points]
    y_values = [p.imag for p in points]
    return x_values, y_values


def plot_coords(x_values, y_values, show=False):
    plt.scatter(x_values,y_values)
    if show:
        plt.show()


def plot_line(x_values, y_values):
    plt.plot(x_values, y_values)
    if show:
        plt.show()


def plot_complex_points(points, show=False):
    x_values, y_values = complex_points_to_coords(points)
    plot_coords(x_values, y_values, show)


def plot_complex_line(p1, p2, show=False):
    x_values, y_values = complex_points_to_coords([p1, p2])
    plot_line(x_values, y_values, show)

from docopt import docopt
import pandas as pd

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

import numpy as np


def main():
    """
    """

    # Get the arguments
    args = docopt("""Matplot the data points from a csv file                     


    Usage:
        plot.py [-d] <file_path> <base_perf> <out_path>

    Arguments:
        <file_path> = path to data_points
        <base_perf> = basis performance
        <out_path> = output for graphic
        
    Options:
        -d, --3Dim  if 3-D data points
    """)

    is_three_dim = args['--3Dim']
    file_path = args['<file_path>']
    base_perf = float(args['<base_perf>'])
    out_path = args['<out_path>']

    df = pd.read_csv(file_path, delimiter=';', header=None)
    tuples = [tuple(x) for x in df.values]

    if is_three_dim:
        plt_3d(tuples, base_perf)
    else:
        plt_2d(tuples, base_perf)


def plt_2d(tuples, base_perf):
    plt.plot(*zip(*tuples), '-bo')

    x, y = zip(*tuples)
    y = [base_perf] * len(y)
    plt.plot(x, y, '-ro')

    plt.show()


def plt_3d(tuples, base_perf):
    X, Y, Z, base_Z = _gen_data(tuples, base_perf)

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    # ax.scatter3D(*zip(*tuples), color='black')
    # ax.plot_wireframe(X, Y, Z, color='black')
    # ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
    #                 cmap='viridis', edgecolor='none')
    ax.contour3D(X, Y, Z, 50, cmap='viridis')
    ax.plot_wireframe(X, Y, base_Z, color='black')

    plt.show()


def _gen_data(tuple, base_perf):
    X = np.array([])
    Y = np.array([])
    z = np.array([])

    for data_point in tuple:
        (_X, _Y, _z) = data_point
        if _X not in X:
            X = np.append(X, _X)
        if _Y not in Y:
            Y = np.append(Y, _Y)
        z = np.append(z, _z)

    Z = np.ndarray((len(X), len(Y)))
    base_Z = np.ndarray((len(X), len(Y)))
    for i in range(len(X)):
        for j in range(len(Y)):
            Z[i][j] = z[i * len(Y) + j]
            base_Z[i][j] = base_perf

    X, Y = np.meshgrid(X, Y)
    return X, Y, Z, base_Z


if __name__ == '__main__':
    main()

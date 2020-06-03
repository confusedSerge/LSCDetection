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
        plot.py [-d] [-s] <file_path> <base_perf> <out_path>

    Arguments:
        <file_path> = path to data_points
        <base_perf> = basis performance
        <out_path> = output for graphic
        
    Options:
        -d, --3Dim  if 3-D data points
        -s, --scater  if scaterplot should be used
    """)

    is_three_dim = args['--3Dim']
    is_scater = args['--scater']
    file_path = args['<file_path>']
    base_perf = float(args['<base_perf>'])
    out_path = args['<out_path>']

    df = pd.read_csv(file_path, delimiter=';', header=None)
    tuples = [tuple(x) for x in df.values]

    if is_three_dim:
        plt_3d(tuples, base_perf, is_scater)
    else:
        plt_2d(tuples, base_perf)


def plt_2d(tuples, base_perf):
    plt.plot(*zip(*tuples), '-bo')

    x, y = zip(*tuples)
    y = [base_perf] * len(y)
    plt.plot(x, y, '-ro')

    plt.show()


def plt_3d(tuples, base_perf, is_scater):
    X, Y, Z, base_Z = _gen_data(tuples, base_perf)

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    if is_scater:
        ax.scatter3D(*zip(*tuples), color='black')
    else:
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

    Z = np.ndarray((len(Y), len(X)))
    base_Z = np.ndarray((len(Y), len(X)))
    for i in range(len(Y)):
        for j in range(len(X)):
            Z[i][j] = z[i * len(X) + j]
            base_Z[i][j] = base_perf

    X, Y = np.meshgrid(X, Y)
    return X, Y, Z, base_Z


if __name__ == '__main__':
    main()

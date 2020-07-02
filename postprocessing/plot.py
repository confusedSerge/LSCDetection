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
        plot.py [-c] [-t] <file_path> <base_perf> <third_optional>

    Arguments:
        <file_path> = path to data_points
        <base_perf> = basis performance data point/s
        <third_optional> = optional
        
    Options:
        -c, --comp  if comparison for ppa
        -t, --three  if three datapoints
    """)

    file_path = args['<file_path>'] 
    base_perf = args['<base_perf>']

    df = pd.read_csv(file_path, delimiter=';', header=None)
    tuples = [tuple(x) for x in df.values]


    df = pd.read_csv(base_perf, delimiter=';', header=None)
    base_tupel = [tuple(x) for x in df.values]

    if args['--three']:
        df = pd.read_csv(args['<third_optional>'], delimiter=';', header=None)
        _third = [tuple(x) for x in df.values]

        plt_ppa_three_fig(tuples, base_tupel, _third)
    else:
        plt_ppa(tuples, base_tupel, args['--comp'])



def plt_ppa(_tuple, base_perf, is_comp):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    
    if not is_comp:
        X, Y, Z, base_Z, scatter_Z = _gen_data(_tuple, base_perf)
        ax.scatter3D(*zip(*scatter_Z), color='red')
    else:
        ax.scatter3D(*zip(*base_perf), color='red')

    ax.scatter3D(*zip(*_tuple), color='black')

    plt.show()

def plt_ppa_three_fig(_first, _sec, _thrid): 
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    ax.scatter3D(*zip(*_first), color='r')
    ax.scatter3D(*zip(*_sec), color='g')
    ax.scatter3D(*zip(*_thrid), color='b')

    plt.show()


def _gen_data(_tuple, base_perf):
    X = np.array([])
    Y = np.array([])
    z = np.array([])

    for data_point in _tuple:
        (_X, _Y, _z) = data_point
        if _X not in X:
            X = np.append(X, _X)
        if _Y not in Y:
            Y = np.append(Y, _Y)
        z = np.append(z, _z)

    Z = np.ndarray((len(Y), len(X)))
    scatter_Z = []
    base_Z = np.ndarray((len(Y), len(X)))
    for i in range(len(Y)):
        for j in range(len(X)):
            Z[i][j] = z[i * len(X) + j]
            base_Z[i][j] = base_perf[j][2]
            scatter_Z.append((X[j], Y[i], base_perf[j][2]))

    X, Y = np.meshgrid(X, Y)
    return X, Y, Z, base_Z, scatter_Z


if __name__ == '__main__':
    main()

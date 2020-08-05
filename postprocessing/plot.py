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
        plot.py (-z) <file_path> <base_perf> [(-t <third_optional>)] [<title> <name1> <name2>]

    Arguments:
        <file_path> = path to data_points
        <base_perf> = basis performance data point/s
        <third_optional> = optional
        <title> = title 
        <name1> = first name
        <name2> = sec name
        
    Options:
        -t, --three  if three datapoints
        -z, --two  if 2d plot should be made 
    """)

    file_path = args['<file_path>'] 
    base_perf = args['<base_perf>']

    df = pd.read_csv(file_path, delimiter=';', header=None)
    tuples = [tuple(x) for x in df.values]


    df = pd.read_csv(base_perf, delimiter=';', header=None)
    base_tupel = [tuple(x) for x in df.values]

    if args['--two']:
        if args['--three']:
            df = pd.read_csv(args['<third_optional>'], delimiter=';', header=None)
            _third = [tuple(x) for x in df.values]
            plot2dthree(tuples, base_tupel, _third, args["<title>"], args["<name1>"], args["<name2>"])
        else:
            plot2d(tuples, base_tupel, args["<title>"], args["<name1>"], args["<name2>"])

    elif args['--three']:
        df = pd.read_csv(args['<third_optional>'], delimiter=';', header=None)
        _third = [tuple(x) for x in df.values]

        plt_ppa_three_fig(tuples, base_tupel, _third)
    else:
        plt_ppa(tuples, base_tupel)



def plt_ppa(_tuple, base_perf):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    
    ax.scatter3D(*zip(*base_perf), color='r')
    ax.scatter3D(*zip(*_tuple), color='g')

    plt.show()

def plt_ppa_three_fig(_first, _sec, _thrid): 
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    ax.scatter3D(*zip(*_first), color='r')
    ax.scatter3D(*zip(*_sec), color='g')
    ax.scatter3D(*zip(*_thrid), color='b')

    plt.show()

def plot2d(_first, _sec, title, name1, name2):
    x, y, z = zip(*_first)
    x_, y_, z_ = zip(*_sec)
    
    plt.plot(y, z, color='c')
    plt.plot(y_, z_, color='m')
    # plt.legend()
    plt.title(title)
    plt.grid()
    plt.show()

def plot2dthree(_first, _sec, _third, title, name1, name2):
    x, y, z = zip(*_first)
    x_, y_, z_ = zip(*_sec)
    x__, y__, z__ = zip(*_third)
    
    plt.plot(y, z, color='c', label=str(name1))
    plt.plot(y_, z_, color='m', label=str(name2))
    plt.plot(y__, z__, color='g', label="baseline")
    plt.legend()
    plt.title(title)
    plt.grid()
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

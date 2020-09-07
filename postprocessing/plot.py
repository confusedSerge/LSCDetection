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
        plot.py <outpath> <file_path> [(-p | -z <base_perf>)] [(-t <third_optional>)] [<title> <name1> <name2> <xlabel> <ylabel>]

    Arguments:
        <outpath> = outpath
        <file_path> = path to data_points
        <base_perf> = basis performance data point/s
        <third_optional> = optional
        <title> = title 
        <name1> = first name
        <name2> = sec name
        
    Options:
        -t, --three  if three datapoints
        -z, --two  if 2d plot should be made 
        -p, --pearson  if pearson file
    """)

    file_path = args['<file_path>'] 
    base_perf = args['<base_perf>']

    df = pd.read_csv(file_path, delimiter=';', header=None)
    tuples = [tuple(x) for x in df.values]

    if args['--two']:
        df = pd.read_csv(base_perf, delimiter=';', header=None)
        base_tupel = [tuple(x) for x in df.values]

        if args['--three']:
            df = pd.read_csv(args['<third_optional>'], delimiter=';', header=None)
            _third = [tuple(x) for x in df.values]

            plot2dthree(tuples, base_tupel, _third, args["<title>"], args["<name1>"], args["<name2>"], args["<xlabel>"], args["<ylabel>"], args["<outpath>"])
        else:
            plot2d(tuples, base_tupel, args["<title>"], args["<name1>"], args["<name2>"], args["<xlabel>"], args["<ylabel>"], args["<outpath>"])

    elif args['--pearson']:
        plt_pearson(tuples, args["<title>"], args["<outpath>"])

def plt_pearson(file, title, outpath):
    x, y, z = zip(*file)

    plt.ylim((0, 1))
    if scale_check(z) or scale_check(y):
        plt.ylim((-1, 1))

    plt.plot(x, y, color='c', label='Pearson Correlation Coefficient')    
    plt.plot(x, z, color='m', label='P-Value')  
    plt.legend()
    plt.title(title)
    plt.xlabel("Dimensions")
    plt.grid()
    # plt.show()
    plt.savefig(outpath)
  


def plot2d(_first, _sec, title, name1, name2, x_label, y_label, outpath):
    x, y, z = zip(*_first)
    x_, y_, z_ = zip(*_sec)

    plt.ylim((0, 1))
    if scale_check(z) or scale_check(z_):
        plt.ylim((-1, 1))
    
    plt.plot(y, z, color='c', label=str(name1))
    plt.plot(y_, z_, color='m', label="baseline")
    plt.legend()
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid()
    # plt.show()
    plt.savefig(outpath)

def plot2dthree(_first, _sec, _third, title, name1, name2, x_label, y_label, outpath):
    x, y, z = zip(*_first)
    x_, y_, z_ = zip(*_sec)
    x__, y__, z__ = zip(*_third)
    

    plt.ylim((0, 1))
    if scale_check(z) or scale_check(z_) or scale_check(z__):
        plt.ylim((-1, 1))

    plt.plot(y, z, color='c', label=str(name1))
    plt.plot(y_, z_, color='m', label=str(name2))
    plt.plot(y__, z__, color='g', label="baseline")
    plt.legend()
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid()
    # plt.show()
    plt.savefig(outpath)

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

def scale_check(arr: list):
    for i in arr:
        if i < 0:
            return True
    return False

if __name__ == '__main__':
    main()

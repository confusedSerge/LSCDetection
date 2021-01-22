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
        plot.py <outpath> <file_path> <base_perf> <title> <name1> <name2> <xlabel> <ylabel>


    Arguments:
        <outpath> = outpath
        <file_path> = path to data_points
        <base_perf> = basis performance data point/s
        <title> = title 
        <name1> = first name
        <name2> = sec name
        <xlabel> = x-axis label 
        <ylabel> = y-axis label
    """)

    df = pd.read_csv(args['<file_path>'], delimiter=';', header=None)
    tuples = [tuple(x) for x in df.values]

    df = pd.read_csv(args['<base_perf>'], delimiter=';', header=None)
    base_tupel = [tuple(x) for x in df.values]

    plot2d(tuples, base_tupel, args["<title>"], args["<name1>"],
           args["<name2>"], args["<xlabel>"], args["<ylabel>"], args["<outpath>"])


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
    plt.savefig(outpath, dpi=300)


if __name__ == '__main__':
    main()

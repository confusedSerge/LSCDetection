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
        plot.py <outpath> <first> <sec> <base>


    Arguments:
        <outpath> = outpath
        <first> = path to data_points
        <sec> = basis performance data point/s
        <base> = optional

    """)

    df = pd.read_csv(args['<file_path>'], delimiter=';', header=None)
    first = [tuple(x) for x in df.values]

    df = pd.read_csv(args['<sec>'], delimiter=';', header=None)
    sec = [tuple(x) for x in df.values]

    df = pd.read_csv(args['<base>'], delimiter=';', header=None)
    base = [tuple(x) for x in df.values]

    plot2dthree(first, sec, base, args["<outpath>"])


def plot2dthree(_first, _sec, _third, outpath):
    x, y, z = zip(*_first)
    x_, y_, z_ = zip(*_sec)
    x__, y__, z__ = zip(*_third)

    plt.ylim((0, 1))
    plt.xlim((0, 25))

    plt.plot(y, z, color='b', label='STA')
    plt.plot(y_, z_, color='c', label='SEP')
    plt.plot(y__, z__, ':', color='grey', label="baseline")
    plt.legend()
    plt.xlabel('m')
    plt.ylabel('Performance')
    # plt.show()
    plt.savefig(outpath, dpi=300)


if __name__ == '__main__':
    main()

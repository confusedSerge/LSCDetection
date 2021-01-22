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
        plot.py <outpath> <first> <sec> <third> <fourth>

    Arguments:
        <outpath> = outpath
        <first> = path to data_points
        <sec> = basis performance data point/s
        <third> = optional
        <fourth> = fourth

    """)

    df = pd.read_csv(args['<first>'], delimiter=';', header=None)
    first = [tuple(x) for x in df.values]

    df = pd.read_csv(args['<sec>'], delimiter=';', header=None)
    sec = [tuple(x) for x in df.values]

    df = pd.read_csv(args['<third>'], delimiter=';', header=None)
    third = [tuple(x) for x in df.values]

    df = pd.read_csv(args['<fourth>'], delimiter=';', header=None)
    fourth = [tuple(x) for x in df.values]

    plot2d4data(tuples, sec, third, fourth, args["<outpath>"])


def plot2d4data(first, _sec, _third, _fourth, outpath):
    x, y, z = zip(*_first)
    xs, ys, zs = zip(*_sec)
    xt, yt, zt = zip(*_third)
    xf, yf, zf = zip(*_fourth)

    plt.ylim((0, 1))
    plt.xlim((0, 25))
    plt.plot(y, z, color='c', label="sde")
    plt.plot(ys, zs, color='#6adb07', label="puk")
    plt.plot(yt, zt, color='b', label="baseline sde")
    plt.plot(yf, zf, color='g', label="baseline puk")
    # plt.plot(alpha, sdewac, color='c', label='sde')
    # plt.plot(alpha, pukwac, color='#6adb07', label='puk')
    # plt.plot(alpha, sde_base, color='b', label='baseline sde')
    # plt.plot(alpha, puk_base, color='g', label='baseline puk')
    plt.legend(loc='lower right')
    plt.xlabel("m")
    plt.ylabel("Perfromance")
    # plt.grid()
    # plt.show()
    plt.savefig(outpath, dpi=300)


if __name__ == '__main__':
    main()

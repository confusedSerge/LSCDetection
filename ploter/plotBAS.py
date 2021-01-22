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
        plot.py <outpath> <file_path>


    Arguments:
        <outpath> = outpath
        <file_path> = path to data_points
    """)

    df = pd.read_csv(args['<file_path>'], delimiter=';', header=None)
    data = [tuple(x) for x in df.values]

    plotBaseAndSuch(data, args['<outpath>'])


def plotBaseAndSuch(_first, outpath):
    # print(_first)
    _first.sort(key=lambda x: x[1])
    name, baseperf, sta, sep = zip(*_first)

    plt.ylim((0, 1))
    # plt.xlim((0, 25))
    plt.xticks(rotation=300)
    plt.plot(name[0:11], baseperf[0:11], 'o:', color='gray', label="baseline")
    plt.plot(name[11:], baseperf[11:], 'o:', color='gray')
    plt.plot(name, sta, 'o', color='#b30000', label="STA")
    plt.plot(name, sep, 'o', color='#ff4d4d', label="SEP+PA")
    # plt.plot(name, sta, 'o', color='b', label="STA")
    # plt.plot(name, sep, 'o', color='c', label="SEP+PA")
    plt.legend(loc='lower right')
    # plt.xlabel("PCs removed")
    plt.ylabel("Perfromance")
    # plt.grid()
    # plt.show()

    plt.gcf().subplots_adjust(bottom=0.15)
    plt.savefig(outpath, dpi=300)


if __name__ == '__main__':
    main()

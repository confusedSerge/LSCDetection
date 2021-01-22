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
        plot.py <outpath> <file_path> <title>


    Arguments:
        <outpath> = outpath
        <file_path> = path to data_points
        <title> = title 
    """)

    file_path = args['<file_path>']

    df = pd.read_csv(file_path, delimiter=';', header=None)
    tuples = [tuple(x) for x in df.values]

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
    plt.savefig(outpath, dpi=300)


if __name__ == '__main__':
    main()

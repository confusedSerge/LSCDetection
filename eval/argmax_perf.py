import sys
import glob
from typing import List
from docopt import docopt
import numpy as np

sys.path.append('./modules/')


def main():
    """
    Evaluation for ppa results
    """

    # Get the arguments
    args = docopt('''Evaluation for ppa results

        Usage:
            argmax_perf.py <src_path>

            <src_path> = path to files to evaluate
        ''')

    src_path = args['<src_path>']

    # read files from directory
    for _file in glob.glob("{}/*.csv".format(src_path)):
        f_open = open(_file, 'r')

        performance = []

        for lines in f_open.readlines():
            values = lines.split(';')
            performance.append(float(values[2]))

        print(_file.rsplit('/')[-1])
        print('argmax: {}\nperformance: {}\n'.format(calc_argmax(performance), performance[calc_argmax(performance)]))

        f_open.close()


def calc_argmax(values) -> float:
    return np.argmax(values)


def calc_mean(values) -> float:
    return np.mean(values)


if __name__ == '__main__':
    main()

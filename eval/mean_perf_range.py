import sys
import glob
import time
import logging
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
            mean_perf_range.py <sta> <sep>

            <sta> = path to sta files to evaluate
            <sep> = path to sep files to evaluate
        ''')

    sta = args['<sta>']
    sep = args['<sep>']

    # actual evaluation

    # var reservation
    # var for src
    performance_sta = []
    performance_sep = []

    # read files from sta directory
    for file in glob.glob("{}/*.csv".format(sta)):
        f_open = open(file, 'r')

        tmp_performance = []

        for lines in f_open.readlines():
            values = lines.split(';')
            tmp_performance.append(float(values[2]))

        performance_sta.append(tmp_performance[0:6])

        f_open.close()

    # read files from sep directory
    for file in glob.glob("{}/*.csv".format(sep)):
        f_open = open(file, 'r')

        tmp_performance = []

        for lines in f_open.readlines():
            values = lines.split(';')
            tmp_performance.append(float(values[2]))

        performance_sep.append(tmp_performance[0:6])

        f_open.close()

    
    print('mean for 0 to 5: {}'.format(np.mean(np.subtract(np.mean(performance_sta, axis=1), np.mean(performance_sep, axis=1)))))
    


def calc_argmax(values) -> float:
    # values = stupid_conversion(values)
    return np.mean(np.argmax(values, axis=1))


def calc_mean(values) -> float:
    return np.mean(values)


def calc_max_mean(values) -> float:
    return np.mean(np.max(values, axis=1))


def calc_fixed_param_mean(values) -> float:
    return np.mean(values, axis=0)

def mode_argmax(values) -> dict:
    dict_ = {}

    val = np.argmax(values, axis=1)    

    for i in val:
            dict_[i] = dict_.get(i, 0) + 1

    return dict_

if __name__ == '__main__':
    main()

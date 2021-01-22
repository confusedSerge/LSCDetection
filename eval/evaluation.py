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
            ppa.py <src_path> <base_path>

            <src_path> = path to files to evaluate
            <base_path> = path to base files to evaluate
        ''')

    src_path = args['<src_path>']
    base_path = args['<base_path>']
    # out_path = args['<out_path>']

    # logging time
    logging.basicConfig(
        format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    logging.info(__file__.upper())
    start_time = time.time()

    # actual evaluation

    # var reservation
    # var for src
    performance = []

    # var for baseline
    base_performance = []

    # read files from directory
    for file in glob.glob("{}/*.csv".format(src_path)):
        f_open = open(file, 'r')

        tmp_performance = np.array([])

        for lines in f_open.readlines():
            values = lines.split(';')
            tmp_performance = np.append(tmp_performance, float(values[2]))

        performance += [tmp_performance]

        f_open.close()

    for file in glob.glob("{}/*/*.csv".format(base_path)):
        f_open = open(file, 'r')

        values = f_open.readline().split(';')
        base_performance = np.append(base_performance, float(values[2]))

        f_open.close()

    performance = np.array(performance)
    # print(base_performance)

    # printing data
    print("mean argmax mean performance: {}".format(
        calc_mean_argmax(performance)))
    print("mean argmax std performance: {}".format(calc_std_argmax(performance)))

    print()

    print("mean ppa max performance: {}".format(calc_max_mean(performance)))
    print("mean base performance: {}".format(calc_mean(base_performance)))
    print("mean performance diff: {}".format(
        calc_mean(max_vals(performance) - base_performance)))
    print("mean std perf diff: {}".format(
        np.std(max_vals(performance) - base_performance)))

    print()

    # logging time
    logging.info("--- %s seconds ---" % (time.time() - start_time))


def calc_mean_argmax(values: List[List[int]]) -> float:
    return np.mean(np.argmax(values, axis=1))


def calc_std_argmax(values: List[List[int]]) -> float:
    return np.std(np.argmax(values, axis=1))


def calc_mean(values) -> float:
    return np.mean(values)


def calc_max_mean(values: List[List[int]]) -> float:
    return np.mean(np.max(values, axis=1))


def calc_fixed_param_mean(values: List[List[int]]) -> float:
    return np.mean(values, axis=0)


def max_vals(values: List[List[int]]) -> dict:
    max_arr = []
    for perfs in values:
        max_arr.append(np.max(perfs))
    return max_arr


if __name__ == '__main__':
    main()

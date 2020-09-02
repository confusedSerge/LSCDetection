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
            ppa.py <src_path> <base_path> <out_path>

            <src_path> = path to files to evaluate
            <base_path> = path to base files to evaluate
            <out_path> = output path for space
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
    performance_low_c1 = []
    performance_low_c2 = []
    performance_high_c1 = []
    performance_high_c2 = []

    # var for baseline
    base_performance = []
    base_performance_low_c1 = []
    base_performance_low_c2 = []
    base_performance_high_c1 = []
    base_performance_high_c2 = []

    # read files from directory
    for file in glob.glob("{}/*.csv".format(src_path)):
        f_open = open(file, 'r')

        tmp_performance = []
        tmp_performance_low_c1 = []
        tmp_performance_high_c1 = []
        tmp_performance_low_c2 = []
        tmp_performance_high_c2 = []

        for lines in f_open.readlines():
            values = lines.split(';')
            tmp_performance.append(int(values[2]))
            tmp_performance_low_c1.append(int(values[3]))
            tmp_performance_low_c2.append(int(values[4]))
            tmp_performance_high_c1.append(int(values[5]))
            tmp_performance_high_c2.append(int(values[6]))

        performance.append(tmp_performance)
        performance_low_c1.append(tmp_performance_low_c1)
        performance_low_c2.append(tmp_performance_low_c2)
        performance_high_c1.append(tmp_performance_high_c1)
        performance_high_c2.append(tmp_performance_high_c2)

        f_open.close()

    for file in glob.glob("{}/*.csv".format(base_path)):
        f_open = open(file, 'r')

        values = f_open.readline().split(';')
        base_performance.append(int(values[2]))
        base_performance_low_c1.append(int(values[3]))
        base_performance_low_c2.append(int(values[4]))
        base_performance_high_c1.append(int(values[5]))
        base_performance_high_c2.append(int(values[6]))

        f_open.close()

    # printing data
    print("mean argmax performance: {}".format(calc_argmax(performance)))

    print()

    print("mean ppa performance: {}".format(calc_mean(performance)))
    print("mean base performance: {}".format(calc_mean(base_performance)))
    print("mean performance diff: {}".format(
        calc_mean(performance) - calc_mean(base_performance)))

    print()

    print("mean ppa max performance: {}".format(calc_max_mean(performance)))
    print("mean base performance: {}".format(calc_mean(base_performance)))
    print("mean performance diff: {}".format(
        calc_max_mean(performance) - calc_mean(base_performance)))

    print()

    print("mean ppa performance fixed param: {}".format(
        calc_fixed_param_mean(performance)))
    print("mean ppa performance low c1 fixed param: {}".format(
        calc_fixed_param_mean(performance_low_c1)))
    print("mean ppa performance low c2 fixed param: {}".format(
        calc_fixed_param_mean(performance_low_c2)))
    print("mean ppa performance high c1 fixed param: {}".format(
        calc_fixed_param_mean(performance_high_c1)))
    print("mean ppa performance high c2 fixed param: {}".format(
        calc_fixed_param_mean(performance_high_c2)))
    print("mean ppa performance fixed param diff baseline: {}".format(
        np.subtract(calc_fixed_param_mean(performance), calc_mean(base_performance))))
    print("mean ppa performance low c1 fixed param diff baseline: {}".format(
        np.subtract(calc_fixed_param_mean(performance_low_c1), calc_mean(base_performance))))
    print("mean ppa performance low c2 fixed param diff baseline: {}".format(
        np.subtract(calc_fixed_param_mean(performance_low_c2), calc_mean(base_performance))))
    print("mean ppa performance high c1 fixed param diff baseline: {}".format(
        np.subtract(calc_fixed_param_mean(performance_high_c1), calc_mean(base_performance))))
    print("mean ppa performance high c2 fixed param diff baseline: {}".format(
        np.subtract(calc_fixed_param_mean(performance_high_c2), calc_mean(base_performance))))

    # logging time
    logging.info("--- %s seconds ---" % (time.time() - start_time))


def calc_argmax(values: List[List[int]]) -> float:
    return np.mean(np.argmax(values, axis=1))


def calc_mean(values) -> float:
    return np.mean(values)


def calc_max_mean(values: List[List[int]]) -> float:
    return np.mean(np.max(values, axis=1))


def calc_fixed_param_mean(values: List[List[int]]) -> float:
    return np.mean(values, axis=0)


if __name__ == '__main__':
    main()

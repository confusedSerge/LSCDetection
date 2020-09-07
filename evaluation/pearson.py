import sys
import time
import logging
from typing import List
from docopt import docopt
from scipy import stats as sts
import pandas as pd


def main():
    """
    Pearson Correlation evaluation
    """

    # Get the arguments
    args = docopt('''Evaluation of stats, a la pearson correlation

        Usage:
            pearson.py <first> <sec>

            <first> = path to first file for evaluation
            <sec> = path to second file for evaluation
        ''')

    first = args['<first>']
    sec = args['<sec>']

    # logging time
    logging.basicConfig(
        format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    logging.info(__file__.upper())
    start_time = time.time()

    # actual evaluation

    df = pd.read_csv(first, delimiter=';', header=None)
    first = [x[2] for x in df.values]


    df = pd.read_csv(sec, delimiter=';', header=None)
    sec = [x[2] for x in df.values]

    print('{};{}'.format(*sts.pearsonr(first, sec)))

    # logging time
    logging.info("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    main()

import sys

sys.path.append('./modules/')

from docopt import docopt
import logging
import time
from utils_ import Space


def main():
    """
    PPA + dimensional reduction
    """

    # Get the arguments
    args = docopt('''PPA and dimensional reduction.

        Usage:
            algo_n.py <matrixPath> <outPath> <threshold> <new_dim> 

            <matrixPath> = path to matrix
            <outPath> = output path for space
            <threshold> = threshold
            <new_dim> = new dimension after algorithm 
        ''')

    matrix_path = args['<matrixPath>']
    out_path = args['<outPath>']
    threshold = args['<threshold>']
    new_dim = args['<new_dim>']

    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    logging.info(__file__.upper())
    start_time = time.time()

    # Load matrices and rows
    try:
        space = Space(matrix_path, format='npz')
        _format_flag = 'npz'
    except ValueError:
        space = Space(matrix_path, format='w2v')
        _format_flag = 'w2v'

    # PPA + dim reduction
    space.algo_n(int(new_dim), int(threshold))

    # Save the matrix
    space.save(out_path, format=_format_flag)

    logging.info("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    main()

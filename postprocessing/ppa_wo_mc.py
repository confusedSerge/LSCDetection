from utils_ import Space
import time
import logging
from docopt import docopt
import sys

sys.path.append('./modules/')


def main():
    """
    Post Processing Algorithm for eliminating common vector in word
    representations without mean centering
    """

    # Get the arguments
    args = docopt('''PPA for common vector elimination

        Usage:
            ppa.py <matrixPath> <outPath> <threshold>

            <matrixPath> = path to matrix
            <outPath> = output path for space
            <threshold> = threshold
        ''')

    matrix_path = args['<matrixPath>']
    out_path = args['<outPath>']
    threshold = args['<threshold>']

    logging.basicConfig(
        format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    logging.info(__file__.upper())
    start_time = time.time()

    # Load matrices and rows
    try:
        space = Space(matrix_path, format='npz')
        _format_flag = 'npz'
    except ValueError:
        space = Space(matrix_path, format='w2v')
        _format_flag = 'w2v'

    # PPA
    space.ppa_wo_mc(int(threshold))

    # Save the matrix
    space.save(out_path, format=_format_flag)

    logging.info("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    main()

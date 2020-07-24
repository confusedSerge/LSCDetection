from collections import defaultdict
from docopt import docopt
import logging
import time


def main():
    """
    Get frequencies from corpus.
    """

    # Get the arguments
    args = docopt("""Get frequencies from corpus, with inbuilt function of python.

    Usage:
        freq.py <testset> <corpDir> <outPath>
        
    Arguments:
       
        <testset> = path to file with one target per line in first column
        <corpDir> = path to corpus or corpus directory (iterates through files)
        <outPath> = output path for result file
        
    """)

    testset = args['<testset>']
    corp_dir = args['<corpDir>']
    out_path = args['<outPath>']

    logging.basicConfig(
        format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    logging.info(__file__.upper())
    start_time = time.time()

    # Initialize frequency dictionary
    freqs = defaultdict(int)

    # Iterate over words
    corpus_size = 0
    for line in open(corp_dir, 'r', encoding='utf-8').readlines():
        for word in line.strip().split(" "):
            corpus_size += 1
            freqs[word] = freqs[word] + 1

    # Load targets
    with open(testset, 'r', encoding='utf-8') as f_in:
        targets = [line.strip().split('\t')[0] for line in f_in]

    # Write frequency scores
    with open(out_path, 'w', encoding='utf-8') as f_out:
        for target in targets:
            if target in freqs:
                f_out.write('\t'.join((target, str(freqs[target])+'\n')))
            else:
                f_out.write('\t'.join((target, 'nan'+'\n')))

    logging.info('tokens: %d' % (corpus_size))
    logging.info('types: %d' % (len(freqs.keys())))
    logging.info("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    main()

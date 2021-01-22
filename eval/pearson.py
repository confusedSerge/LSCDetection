import sys
import glob

from docopt import docopt

from scipy import stats as sts
import numpy as np


def main():
    """
    Pearson Correlation evaluation
    """

    # Get the arguments
    args = docopt('''Evaluation of stats, a la pearson correlation

        Usage:
            pearson.py <first> 

            <first> = path to first file for evaluation
        ''')

    src_path = args['<first>']

    pear_performance_isotropy = []
    # pear_performance_centroid = []
    pear_performance_frequency = []
    # pear_isotropy_frequency = []
    # pear_isotropy_centroid = []
    # pear_centroid_frequency = []
    pear_param_iso = []
    pear_param_frq = []

    # read files from directory
    for file in glob.glob("{}/*.csv".format(src_path)):
        f_open = open(file, 'r')

        performance = []
        freq_bias = []
        isotropy = []
        centroid_len = []

        for lines in f_open.readlines():
            values = lines.split(';')
            performance.append(float(values[2]))
            freq_bias.append(float(values[13]))
            isotropy.append(float(values[16]))
            centroid_len.append(float(values[18]))

        f_open.close()

        pear_performance_isotropy.append(sts.pearsonr(performance, isotropy))
        # pear_performance_centroid.append(sts.pearsonr(performance, centroid_len))
        pear_performance_frequency.append(sts.pearsonr(performance, freq_bias))
        # pear_isotropy_centroid.append(sts.pearsonr(isotropy, centroid_len))
        # pear_isotropy_frequency.append(sts.pearsonr(isotropy, freq_bias))
        # pear_centroid_frequency.append(sts.pearsonr(centroid_len, freq_bias))


        pear_param_iso.append(sts.pearsonr(list(range(0, 26)), isotropy))
        pear_param_frq.append(sts.pearsonr(list(range(0, 26)), freq_bias))
        

    print('Param<>Isot: {}, max: {}, min: {}'.format(np.mean(pear_param_iso, axis=0), np.max(pear_param_iso, axis=0), np.min(pear_param_iso, axis=0)))
    print('Param<>Freq: {}, max: {}, min: {}'.format(np.mean(pear_param_frq, axis=0), np.max(pear_param_frq, axis=0), np.min(pear_param_frq, axis=0)))
    

    print('Perf<>Isot: {}, max: {}, min: {}'.format(np.mean(pear_performance_isotropy, axis=0), np.max(pear_performance_isotropy, axis=0), np.min(pear_performance_isotropy, axis=0)))
    # print('Perf<>Cent: {}, max: {}, min: {}'.format(np.mean(pear_performance_centroid, axis=0), np.max(pear_performance_centroid, axis=0), np.min(pear_performance_centroid, axis=0)))
    print('Perf<>Freq: {}, max: {}, min: {}'.format(np.mean(pear_performance_frequency, axis=0), np.max(pear_performance_frequency, axis=0), np.min(pear_performance_frequency, axis=0)))
    # print('Isot<>Cent: {}, max: {}, min: {}'.format(np.mean(pear_isotropy_centroid, axis=0), np.max(pear_isotropy_centroid, axis=0), np.min(pear_isotropy_centroid, axis=0)))
    # print('Isot<>Freq: {}, max: {}, min: {}'.format(np.mean(pear_isotropy_frequency, axis=0), np.max(pear_isotropy_frequency, axis=0), np.min(pear_isotropy_frequency, axis=0)))
    # print('Cent<>Freq: {}, max: {}, min: {}'.format(np.mean(pear_centroid_frequency, axis=0), np.max(pear_centroid_frequency, axis=0), np.min(pear_centroid_frequency, axis=0)))


#     print('{};{}'.format(*sts.pearsonr(first, sec)))

if __name__ == '__main__':
    main()

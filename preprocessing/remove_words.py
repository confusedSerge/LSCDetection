from docopt import docopt
import logging
import time


def main():
    """
    Preprocess corpus (remove low-frequency words, etc.).
    """

    # Get the arguments
    args = docopt("""Preprocess matrix

    Usage:
        remove_words.py <input_matrix> <dict> <outPath>
        
    Arguments:
       
        <input_matrix> = path to matrix
        <dict> = file with words to keep
        <outPath> = output path
        
    """)

    input_matrix = args['<input_matrix>']
    _dict = args['<dict>']
    out_path = args['<outPath>']

    logging.basicConfig(
        format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    logging.info(__file__.upper())
    start_time = time.time()

    # generate word array
    target_word_file = open(_dict, 'r', encoding='utf-8')
    target_words = []
    for line in target_word_file.readlines():
        in_words = line.strip().split(" ")
        if in_words[0] not in target_words:
            target_words.append(in_words[0])
        if in_words[1] not in target_words:
            target_words.append(in_words[1])

    # generate new header
    matrix = open(input_matrix, 'r', encoding='utf-8')
    header = True
    head = []
    for line in matrix.readlines():
        if header:
            head = [int(numeric_string) for numeric_string in line.split(" ")]
            head[0] = 0
            header = False
        if clean_line(line) in target_words:
            head[0] += 1

    head = "{} {}\n".format(*head)

    # Write output
    matrix = open(input_matrix, 'r', encoding='utf-8')
    with open(out_path, 'w', encoding='utf-8') as f_out:
        f_out.write(head)
        for line in matrix.readlines():
            if clean_line(line) in target_words:
                f_out.write(line)

    logging.info("--- %s seconds ---" % (time.time() - start_time))


def clean_line(line: str):
    word: str = line.strip().split(" ")[0]
    if word.endswith('_'):
        return word.rstrip('_')
    return word


if __name__ == '__main__':
    main()

from argparse import *


def main():

    parser = ArgumentParser(description='Command Line Tool for Plagiarism Detection')

    parser.add_argument(
        '-f', '--files', required=True, nargs=2,
        help='Two files to compare for plagiarism'
    )

    parser.add_argument('-s', '--synonyms', required=True, help='Synonyms file')

    parser.add_argument('-t', '--tuple_size', type=int, help='Size of the tuple')

    parser = parser.parse_args()

    [file1, file2] = parser.files
    synonyms = parser.synonyms
    tuple_size = parser.tuple_size


if __name__ == '__main__':
    main()
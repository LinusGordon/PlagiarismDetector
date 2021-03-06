from argparse import *
from plagiarism_detector import PlagiarismDetector


def main():

    parser = ArgumentParser(description='Command Line Tool for Plagiarism Detection')

    parser.add_argument('-f', '--files', required=True, nargs=2,
                        help='Two files to compare for plagiarism',
                        )
    parser.add_argument('-s', '--synonyms', required=True, help='Synonyms file',)
    parser.add_argument('-t', '--tuple_size', type=int, help='Size of the tuple',
                        default=PlagiarismDetector.DEFAULT_TUPLE_SIZE,
                        )

    parser = parser.parse_args()

    print(PlagiarismDetector(parser.files,
                             parser.synonyms,
                             parser.tuple_size
                             ).get_percentage_plagiarized(),
          )


if __name__ == '__main__':
    main()
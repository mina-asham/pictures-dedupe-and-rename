import glob
import logging
import os
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, SUPPRESS
from argparse import ArgumentTypeError
from sys import maxsize

import pictures

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(name)s %(levelname)s %(message)s')


def directory_type(arg):
    if not os.path.isdir(arg):
        raise ArgumentTypeError('{} is not a valid directory!'.format(arg))

    return os.path.abspath(arg)


def patterns_type(arg):
    patterns = arg.split(',')
    if len(patterns) == 0:
        raise ArgumentTypeError('{} is an invalid pattern!'.format(arg))

    return patterns


def operations_type(arg):
    if arg == 'dedupe':
        return pictures.dedupe,
    if arg == 'rename':
        return pictures.rename,
    if arg == 'both':
        return pictures.dedupe, pictures.rename

    raise ArgumentTypeError('Invalid operation: {}!'.format(arg))


def parse_arguments():
    parser = ArgumentParser(
        description='Dedupe a set of pictures in a given folder and rename them using the yyyymmdd_HHMMss format',
        formatter_class=lambda prog: ArgumentDefaultsHelpFormatter(prog, max_help_position=maxsize, width=maxsize)
    )
    parser.add_argument('-d', '--directory',
                        type=directory_type,
                        help='input directory for all pictures',
                        default=SUPPRESS,
                        required=True)
    parser.add_argument('-o', '--operations',
                        type=operations_type,
                        help='the operatiosn to perform (dedupe, rename, or both)',
                        default='both')
    parser.add_argument('-p', '--patterns',
                        type=patterns_type,
                        help='the glob patterns for pictures',
                        default='*.jpeg,*.jpg,*.png')

    return parser.parse_args()


def main():
    arguments = parse_arguments()
    for operation in arguments.operations:
        for pattern in arguments.patterns:
            files = glob.glob(os.path.join(arguments.directory, pattern))
            operation(files)


if __name__ == '__main__':
    main()

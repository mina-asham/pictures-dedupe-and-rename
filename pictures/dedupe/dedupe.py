import filecmp
import itertools
import os

from pictures.loggers import logger_from

logger = logger_from(__name__)


def dedupe(filenames, prefer_shorter=True):
    for filename1, filename2 in itertools.combinations(filenames, 2):
        if filecmp.cmp(filename1, filename2):
            file_to_delete = max(filename1, filename2) if prefer_shorter else min(filename1, filename2)
            os.remove(file_to_delete)
            logger.info('Deleted: %s', file_to_delete)

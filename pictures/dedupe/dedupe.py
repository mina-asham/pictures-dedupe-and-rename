import filecmp
import itertools
import logging
import os

logger = logging.getLogger(__name__)


def dedupe(filenames, prefer_shorter=True):
    deleted = set()
    for filename1, filename2 in itertools.combinations(filenames, 2):
        if filename1 not in deleted and filename2 not in deleted and filecmp.cmp(filename1, filename2):
            file_to_delete = max(filename1, filename2) if prefer_shorter else min(filename1, filename2)
            os.remove(file_to_delete)
            deleted.add(file_to_delete)
            logger.info('Deleted: %s', file_to_delete)

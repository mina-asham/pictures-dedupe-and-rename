import filecmp
import itertools
import logging
import os

logger = logging.getLogger(__name__)


def dedupe(filenames, prefer_shorter=True):
    deleted = set()
    for filename1, filename2 in itertools.combinations(filenames, 2):
        if filename1 not in deleted and filename2 not in deleted and filecmp.cmp(filename1, filename2):
            file_to_delete, original_file = sorted([filename1, filename2], reverse=prefer_shorter)
            os.remove(file_to_delete)
            deleted.add(file_to_delete)
            logger.info('Deleted: %s (duplicate of: %s)', file_to_delete, original_file)

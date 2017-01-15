import logging
import os
import time

import exifread

logger = logging.getLogger(__name__)


def rename(filenames):
    for filename in filenames:
        new_filename = _new_filename_from(filename)
        if new_filename:
            os.rename(filename, new_filename)
            logger.info('Renamed %s to %s', filename, new_filename)


def _new_filename_from(filename):
    dirname = os.path.dirname(filename)
    date_created = _date_created_from(filename)
    _, extension = os.path.splitext(filename)
    base_filename = os.path.basename(filename)

    if not date_created:
        logger.warning('File %s does not have EXIF tags!', filename)
        return None

    if base_filename.startswith(date_created):
        return None  # Already properly formatted, nothing to do here

    new_filename = os.path.join(dirname, '{}{}'.format(date_created, extension))

    if not os.path.isfile(new_filename):
        return new_filename

    for i in range(1, 1001):
        new_filename = os.path.join(dirname, '{}_{}{}'.format(date_created, i, extension))
        if not os.path.isfile(new_filename):
            return new_filename

    logger.warning('File %s has more than 1000 copies with the same name!')
    return None


def _can_parse_date(date_time):
    try:
        time.strptime(date_time, '%Y:%m:%d %H:%M:%S')
        return True
    except (TypeError, ValueError):
        return False


def _date_created_from(filename):
    with open(filename, 'rb') as f:
        tags = exifread.process_file(f)

    date_time_original = tags.get('EXIF DateTimeOriginal')
    if not date_time_original or not _can_parse_date(date_time_original.values):
        return None

    return date_time_original.values.replace(':', '').replace(' ', '_')

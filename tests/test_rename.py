from unittest import TestCase
from unittest import mock
from unittest.mock import MagicMock

from exifread import IfdTag

from pictures.rename import rename
from tests import test_helpers


def ifd_tag_from(date_time_original):
    return IfdTag(None, None, None, date_time_original, None, None)


class MockFile(object):
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass


def create_mock_process_file(files):
    return lambda f_mock: files[f_mock.filename]


def create_mock_isfile(files):
    return lambda f: f in files


class TestRename(TestCase):
    FILES = {
        r'C:\dir\no_exif_tags.jpeg': {},

        r'C:\dir\timestamp_does_not_exist.jpeg': {'EXIF DateTimeOriginal': ifd_tag_from('2016:10:29 15:43:56')},  # 1 check

        r'C:\dir\timestamp_does_exist.jpeg': {'EXIF DateTimeOriginal': ifd_tag_from('2016:02:04 12:03:35')},  # 2 checks
        r'C:\dir\20160204_120335.jpeg': {'EXIF DateTimeOriginal': ifd_tag_from('2016:02:04 12:03:35')},

        r'C:\dir\timestamp_does_exist_multiple.jpeg': {'EXIF DateTimeOriginal': ifd_tag_from('2017:01:03 14:23:45')},  # 4 checks
        r'C:\dir\20170103_142345.jpeg': {'EXIF DateTimeOriginal': ifd_tag_from('2017:01:03 14:23:45')},
        r'C:\dir\20170103_142345_1.jpeg': {'EXIF DateTimeOriginal': ifd_tag_from('2017:01:03 14:23:45')},
        r'C:\dir\20170103_142345_2.jpeg': {'EXIF DateTimeOriginal': ifd_tag_from('2017:01:03 14:23:45')}
    }

    @mock.patch('os.rename')
    @mock.patch('os.path.isfile', side_effect=create_mock_isfile(FILES))
    @mock.patch('exifread.process_file', side_effect=create_mock_process_file(FILES))
    @mock.patch('builtins.open', side_effect=MockFile)
    def test_rename(self, mock_open: MagicMock, mock_process_file: MagicMock, mock_isfile: MagicMock, mock_rename: MagicMock):
        rename(self.FILES)

        self.assertEquals(mock_open.mock_calls, test_helpers.calls_from(zip(self.FILES.keys(), ['rb'] * len(self.FILES))))
        self.assertEquals(mock_process_file.call_count, len(self.FILES))
        self.assertEquals(mock_isfile.call_count, 7)  # number of checks
        self.assertEquals(mock_rename.mock_calls, test_helpers.calls_from([
            (r'C:\dir\timestamp_does_not_exist.jpeg', r'C:\dir\20161029_154356.jpeg'),
            (r'C:\dir\timestamp_does_exist.jpeg', r'C:\dir\20160204_120335_1.jpeg'),
            (r'C:\dir\timestamp_does_exist_multiple.jpeg', r'C:\dir\20170103_142345_3.jpeg')
        ]))
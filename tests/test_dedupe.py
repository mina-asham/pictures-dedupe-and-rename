from unittest import TestCase
from mock import mock

from pictures.dedupe import dedupe
from tests import helpers


def create_mock_cmp(equal_files):
    return lambda f1, f2: f1 in equal_files and f2 in equal_files


class TestDedupe(TestCase):
    EQUAL_FILES = ['filename1', 'filename2', 'filename3']
    NON_EQUAL_FILES = ['filename4', 'filename5']
    FILES = EQUAL_FILES + NON_EQUAL_FILES

    @mock.patch('os.remove')
    @mock.patch('filecmp.cmp', side_effect=create_mock_cmp(EQUAL_FILES))
    def test_dedupe_prefer_shorter(self, mock_cmp, mock_remove):
        dedupe(self.FILES)
        self.assertEquals(mock_cmp.mock_calls, helpers.calls_from([
            ('filename1', 'filename2'),
            ('filename1', 'filename3'),
            ('filename1', 'filename4'),
            ('filename1', 'filename5'),
            ('filename4', 'filename5')
        ]))
        self.assertEquals(mock_remove.mock_calls, helpers.calls_from([
            ('filename2',),
            ('filename3',)
        ]))

    @mock.patch('os.remove')
    @mock.patch('filecmp.cmp', side_effect=create_mock_cmp(EQUAL_FILES))
    def test_dedupe_prefer_longer(self, mock_cmp, mock_remove):
        dedupe(self.FILES, prefer_shorter=False)
        self.assertEquals(mock_cmp.mock_calls, helpers.calls_from([
            ('filename1', 'filename2'),
            ('filename2', 'filename3'),
            ('filename3', 'filename4'),
            ('filename3', 'filename5'),
            ('filename4', 'filename5')
        ]))
        self.assertEquals(mock_remove.mock_calls, helpers.calls_from([
            ('filename1',),
            ('filename2',)
        ]))

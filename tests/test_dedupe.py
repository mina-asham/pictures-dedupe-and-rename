import itertools
from unittest import TestCase
from unittest import mock
from unittest.mock import MagicMock

from pictures.dedupe import dedupe
from tests import test_helpers


def create_mock_cmp(equal_files):
    return lambda f1, f2: f1 in equal_files and f2 in equal_files


class TestDedupe(TestCase):
    EQUAL_FILES = ['filename1', 'filename2']
    NON_EQUAL_FILES = ['filename3', 'filename4']
    FILES = EQUAL_FILES + NON_EQUAL_FILES

    @mock.patch('os.remove')
    @mock.patch('filecmp.cmp', side_effect=create_mock_cmp(EQUAL_FILES))
    def test_dedupe_prefer_shorter(self, mock_cmp: MagicMock, mock_remove: MagicMock):
        dedupe(self.FILES)
        self.assertEquals(mock_cmp.mock_calls, test_helpers.calls_from(itertools.combinations(self.FILES, 2)))
        mock_remove.assert_called_once_with('filename1')

    @mock.patch('os.remove')
    @mock.patch('filecmp.cmp', side_effect=create_mock_cmp(EQUAL_FILES))
    def test_dedupe_prefer_longer(self, mock_cmp: MagicMock, mock_remove: MagicMock):
        dedupe(self.FILES, prefer_shorter=False)
        self.assertEquals(mock_cmp.mock_calls, test_helpers.calls_from(itertools.combinations(self.FILES, 2)))
        mock_remove.assert_called_once_with('filename2')

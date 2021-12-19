import pytest

from homework09.hw1 import merge_sorted_files

from .test_contextmanager import create_files

TEXT_1 = "1\n3\n5\n7"

TEXT_2 = "21\n23\n25\n27"

TEXT_3 = "2\n4\n6\n8"

TEXT_ERR = "2 2\n"


def test_merge_files_attrs():
    with create_files([TEXT_1, TEXT_2, TEXT_3]) as files_created:
        result = merge_sorted_files(files_created)
        assert hasattr(result, "__iter__")
        assert hasattr(result, "__next__")


def test_merge_files_values():
    with create_files([TEXT_1, TEXT_2, TEXT_3]) as files_created:
        result = list(merge_sorted_files(files_created))
        assert isinstance(result, list)

        sorted_results = sorted(result)
        assert result == sorted_results


def test_merge_files_error():
    with create_files([TEXT_1, TEXT_2, TEXT_ERR]) as files_created:
        with pytest.raises(ValueError):
            result = list(merge_sorted_files(files_created))

import pytest

from homework04.task_1_read_file import read_magic_number


def test_True(create_file_True):
    assert read_magic_number(create_file_True) is True


def test_False(create_file_False):
    assert read_magic_number(create_file_False) is False


def test_Error(create_file_Error):
    with pytest.raises(ValueError):
        read_magic_number(create_file_Error)

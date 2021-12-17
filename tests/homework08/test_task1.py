from unittest import mock

import pytest

from homework08.task1 import KeyValueStorage

test_data = [
    (["name", "kek"], str),
    (["last_name", "top"], str),
    (["power", 9001], int),
    (["song", 1001], int),
]


@pytest.mark.parametrize("test_input, exp_type", test_data)
def test_key_value_no_err(open_file, test_input, exp_type):
    with mock.patch("builtins.open", open_file):
        storage = KeyValueStorage("file_name")
    assert storage[test_input[0]] == test_input[1]
    assert isinstance(storage[test_input[0]], exp_type)


def test_key_value_err(open_file_err):
    with pytest.raises(ValueError):
        with mock.patch("builtins.open", open_file_err):
            storage = KeyValueStorage("file_name")

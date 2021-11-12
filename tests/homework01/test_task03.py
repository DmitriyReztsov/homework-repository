from random import randint
from unittest import mock

from homework01.task03 import find_maximum_and_minimum


def before(min_value, max_value, min_range, max_range):
    raw_data = [
        randint(min_value, max_value)
        for _ in range(randint(min_range, max_range))
    ]
    read_data = "\n".join(map(str, raw_data))
    mock_open = mock.mock_open(read_data=read_data)
    mi = min(raw_data)
    ma = max(raw_data)
    return mock_open, mi, ma


def test_random():
    mock_open, min, max = before(-100, 100, 5, 50)

    with mock.patch("builtins.open", mock_open):
        result = find_maximum_and_minimum("file_name")
    assert result[0] == min and result[1] == max


def test_same():
    mock_open, min, max = before(100, 100, 5, 50)

    with mock.patch("builtins.open", mock_open):
        result = find_maximum_and_minimum("file_name")
    assert result[0] == min and result[1] == max


def test_one_value():
    mock_open, min, max = before(100, 100, 1, 1)

    with mock.patch("builtins.open", mock_open):
        result = find_maximum_and_minimum("file_name")
    assert result[0] == min and result[1] == max

from unittest import mock

import pytest

from homework01.task03 import find_maximum_and_minimum

test_data = [
    ([1, 1, 3, 4, 5, 6, 7, 8], [1, 8]),
    ([1, 1, 1, 100, 100, 101, 100], [1, 101]),
    ([1, -1, -1, 0, 0, 0, 2, 3, 3], [-1, 3]),
    (
        [
            12,
        ],
        [12, 12],
    ),
]


@pytest.mark.parametrize("test_input, expected", test_data)
def test_random(test_input, expected):
    read_data = "\n".join(map(str, test_input))
    mock_open = mock.mock_open(read_data=read_data)

    with mock.patch("builtins.open", mock_open):
        result = find_maximum_and_minimum("file_name")
    assert result[0] == expected[0] and result[1] == expected[1]

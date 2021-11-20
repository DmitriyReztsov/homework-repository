import string

import pytest

from homework02.hw5 import custom_range

test_data = [
    (([1, 2, 3, 4], 3), ([1, 2])),
    (
        (string.ascii_lowercase, "a", "r", 2),
        (["a", "c", "e", "g", "i", "k", "m", "o", "q"]),
    ),
    (({1: "a", 2: "s", 3: "d", 4: "a", 5: "s"}, 3), ([(1, "a"), (2, "s")])),
    (((1, 2, 3, 4, 5, 6), 6, 4, -1), ([6, 5])),
]


@pytest.mark.parametrize("test_input, expected", test_data)
def test_custom_range(test_input, expected):
    assert custom_range(*test_input) == expected

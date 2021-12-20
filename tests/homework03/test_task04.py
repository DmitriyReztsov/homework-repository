import pytest

from homework03.task04.task04 import is_armstrong

test_data = [
    (1, True),
    (2, True),
    (3, True),
    (4, True),
    (5, True),
    (6, True),
    (7, True),
    (8, True),
    (9, True),
    (153, True),
    (370, True),
    (371, True),
    (407, True),
    (1634, True),
    (-1634, False),
    (8207, False),
    (9475, False),
    (54747, False),
    (92728, False),
    (93054, False),
    (538834, False),
    (1241725, False),
]


@pytest.mark.parametrize("test_input, expected", test_data)
def test_armstrong(test_input, expected):
    assert is_armstrong(test_input) == expected

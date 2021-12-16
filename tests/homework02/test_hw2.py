import pytest

from homework02.hw2 import major_and_minor_elem

test_data = [
    ([1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 2, 2, 3, 3], (1, 4)),
    ([1, 1], (1, 1)),
    ([-1, -1, -1, -1, 0, 0, 0, 0, 2, 3, 3], (-1, 2)),
    (["a", "a", "a", "b"], ("a", "b")),
]


@pytest.mark.parametrize("test_input, expected", test_data)
def test_major_and_minor_elem_positive(test_input, expected):
    assert major_and_minor_elem(test_input) == expected

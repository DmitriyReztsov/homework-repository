import pytest

from homework04.task_5_optional import fizzbuzz

test_data = [
    ([5, 2], "fizz"),
    ([120, 100], "101"),
    ([120, 29], "fizzbuzz"),
    ([120, 49], "buzz"),
]


@pytest.mark.parametrize("test_input, expected", test_data)
def test_fizzbuzz(test_input, expected):
    input, index = test_input
    assert list(fizzbuzz(input))[index] == expected

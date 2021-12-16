import pytest

from homework07.hw2 import backspace_compare

test_data = [
    (["a#c", "b"], False),
    (["ab#c", "ad#c"], True),
    (["#######a########b#######cdt#f######", ""], True),
]


@pytest.mark.parametrize("test_input, expected", test_data)
def test_backspace_compare(test_input, expected):
    assert backspace_compare(test_input[0], test_input[1]) is expected

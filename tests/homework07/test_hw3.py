import pytest

from homework07.hw3 import tic_tac_toe_checker

test_data = [
    ([["0", "*", "0"], ["0", "*", "0"], ["*", "0", "*"]], "draw!"),
    ([["-", "-", "o"], ["-", "o", "o"], ["x", "x", "x"]], "x wins!"),
    ([["-", "-", "O"], ["-", "X", "O"], ["X", "O", "X"]], "unfinished!"),
]

wrong_data = [
    ([["0", "*", "o"], ["0", "*", "0"], ["*", "0", "*"]]),
    ([["-", "-", "o"], ["-", "o", "o"], ["x", "Xx", "x"]]),
    ([["-", "1", "O"], ["z", "X", "R"], ["X", "b", "X"]]),
]


@pytest.mark.parametrize("test_input, expected", test_data)
def test_tic_tac_toe(test_input, expected):
    assert tic_tac_toe_checker(test_input) == expected


@pytest.mark.parametrize("test_input", wrong_data)
def test_tic_tac_toe_wrong_input(test_input):
    with pytest.raises(ValueError):
        tic_tac_toe_checker(test_input)

import io
from contextlib import redirect_stderr, redirect_stdout

import pytest

from homework04.task_3_get_print_output import my_precious_logger

test_data = [
    ("Error: text of error", ["", "Error: text of error", 20]),
    ("No error", ["No error", "", 8]),
]


@pytest.mark.parametrize("test_input, expected", test_data)
def test_my_precious_logger(test_input, expected):
    with redirect_stdout(io.StringIO()) as output:
        with redirect_stderr(io.StringIO()) as errors:
            counter = my_precious_logger(test_input)

    assert output.getvalue() == expected[0]
    assert errors.getvalue() == expected[1]
    assert counter == expected[2]

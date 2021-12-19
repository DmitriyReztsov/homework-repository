import os

import pytest

from homework09.hw3 import universal_file_counter

from .test_contextmanager import create_files

TEXT_1 = "1 2\n3 4\n5 6\n7 8"

TEXT_2 = "21\n23 34\n25 df\n27"

TEXT_3 = (
    "we don't need no education\n"
    "we don't need no thought control\n"
    "no dark sarcasm in the classroom\n"
    "teacher, leave the kids alone"
)

test_data = [
    ([TEXT_1, TEXT_2, TEXT_3], [12, 36]),
    ([TEXT_1, TEXT_2], [8, 14]),
    ([TEXT_2, TEXT_3], [8, 28]),
]


@pytest.mark.parametrize("test_input, expected", test_data)
def test_counter(test_input, expected):
    with create_files(test_input):
        path_to_tests = os.path.abspath("tests/homework09/")
        assert universal_file_counter(path_to_tests, ".txt") == expected[0]
        assert universal_file_counter(path_to_tests, ".txt", str.split) == expected[1]

import pytest

from homework07 import hw1

test_tree = {
    1: 1,
    2: "2",
    "1": "1",
    "first": ["RED", "BLUE", False],
    "second": {
        "simple_key": ["simple value", "1", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "True": False,
        "False": True,
        "complex_key": {
            "key1": "1",
            "key2": "RED",
            3: [2, "lot", "of", "values", {"nested_key": "RED"}],
        },
    },
    "fourth": "RED",
}

test_data = [
    (1, 2),
    ("1", 4),
    ("RED", 6),
    (False, 2),
]


@pytest.mark.parametrize("test_input, expected", test_data)
def test_find_occurence(test_input, expected):
    assert hw1.find_occurrences(test_tree, test_input) == expected

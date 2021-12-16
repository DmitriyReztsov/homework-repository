import pytest

from homework02.hw3 import combinations

test_data = [
    (([1, 2], [3, 4]), ([[1, 3], [1, 4], [2, 3], [2, 4]])),
    (
        (
            [
                "a",
            ],
            ["b", "c"],
        ),
        ([["a", "b"], ["a", "c"]]),
    ),
]


@pytest.mark.parametrize("test_input, expected", test_data)
def test_combinations(test_input, expected):
    numbers_in_result = 1
    for combination in expected:
        numbers_in_result *= len(combination)
    assert combinations(*test_input) == expected


def test_combination_extreme_len():
    test_input = ([n for n in range(5)] for _ in range(5))
    assert len(combinations(*test_input)) == 5 ** 5

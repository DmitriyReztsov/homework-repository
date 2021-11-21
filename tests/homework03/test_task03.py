import pytest

from homework03.task03.task03 import make_filter

test_data = [
    (
        (
            {
                "name": "Bill",
                "last_name": "Gilbert",
                "occupation": "was here",
                "type": "person",
            },
            {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
        ),
        ([{"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"}]),
    ),
    (
        (
            {
                "name": "Bill",
                "last_name": "Gilbert",
                "occupation": "was here",
                "type": "person",
            },
            {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
            {"is_dead": False, "kind": "parrot", "type": "bird", "name": "mono"},
        ),
        (
            [
                {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
                {"is_dead": False, "kind": "parrot", "type": "bird", "name": "mono"},
            ]
        ),
    ),
    (
        (
            {"is_dead": True, "kind": "shepherd", "type": "dog", "name": "polly"},
            {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
            {"is_dead": False, "kind": "parrot", "type": "bird", "name": "mono"},
        ),
        (
            [
                {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
                {"is_dead": False, "kind": "parrot", "type": "bird", "name": "mono"},
            ]
        ),
    ),
]


@pytest.mark.parametrize("test_input, expected", test_data)
def test_filter_one_return(test_input, expected):
    assert make_filter(name="polly", type="bird").apply(test_input) == expected


@pytest.mark.parametrize("test_input, expected", test_data)
def test_filter_two_returns(test_input, expected):
    assert make_filter(kind="parrot", type="bird").apply(test_input) == expected

import pytest

from homework11.hw1 import SimplifiedEnum, SimplifiedEnum2

test_data = [
    (("one", "two", "three"), {"one": "one", "two": "two", "three": "three"}),
    (("one", "two", "three", "two"), {"one": "one", "two": "two", "three": "three"}),
    (("one", "two", "three", "two"), {"four": AttributeError}),
]


@pytest.mark.parametrize("test_input, expected", test_data)
def test_class(test_input, expected):
    class TetsEnums(metaclass=SimplifiedEnum):
        __keys = test_input

    for key, value in expected.items():
        if key != "four":
            assert getattr(TetsEnums, key) == value
        else:
            with pytest.raises(AttributeError):
                assert getattr(TetsEnums, key) == value


@pytest.mark.parametrize("test_input, expected", test_data)
def test_def(test_input, expected):
    class TetsEnums(metaclass=SimplifiedEnum2):
        __keys = test_input

    for key, value in expected.items():
        if key != "four":
            assert getattr(TetsEnums, key) == value
        else:
            with pytest.raises(AttributeError):
                assert getattr(TetsEnums, key) == value

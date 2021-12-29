import pytest

from homework09.hw2 import SupressorCls, supressor_gen


class DoesNotRaise:
    def __init__(self):
        pass

    def __enter__(self):
        pass

    def __exit__(self, *args):
        pass


test_data = [
    ([ValueError, ValueError], DoesNotRaise()),
    ([IndexError, ValueError], pytest.raises(ValueError)),
]

test_data_2 = [
    ([ValueError, "int('a')"], DoesNotRaise()),
    ([IndexError, "[][2]"], DoesNotRaise()),
    ([IndexError, "int('a')"], pytest.raises(ValueError)),
    ([ValueError, "[][2]"], pytest.raises(IndexError)),
]


@pytest.mark.parametrize("test_input, expectation", test_data)
def test_supressor_cls(test_input, expectation):
    with expectation:
        with SupressorCls(test_input[0]):
            raise test_input[1]


@pytest.mark.parametrize("test_input, expectation", test_data)
def test_supressor_gen(test_input, expectation):
    with expectation:
        with supressor_gen(test_input[0]):
            raise test_input[1]


@pytest.mark.parametrize("test_input, expectation", test_data_2)
def test_supressor_cls_values(test_input, expectation):
    with expectation:
        with SupressorCls(test_input[0]):
            exec(test_input[1])


@pytest.mark.parametrize("test_input, expectation", test_data_2)
def test_supressor_gen_values(test_input, expectation):
    with expectation:
        with supressor_gen(test_input[0]):
            exec(test_input[1])

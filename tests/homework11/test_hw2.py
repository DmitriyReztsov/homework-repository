import pytest

from homework11.hw2 import Order


def discount_1(order):
    return order.price * (1 - 0.25)


def discount_2(order):
    return order.price * (1 + 1)


def no_discount(order):
    return order.price


test_data = [(discount_1, 75), (discount_2, 200), (no_discount, 100), (None, 100)]


@pytest.mark.parametrize("test_input, expected", test_data)
def test_strategy(test_input, expected):
    order = Order(price=100, discount=test_input)
    assert order.final_price() == expected

import pytest

from homework02.hw4 import cache


@cache
def func(a, b):
    return (a ** b) ** 2


def test_cache_args():
    v1 = func(12, 1)
    v2 = func(12, 1)
    assert v1 is v2


def test_cache_kwargs():
    v1 = func(a=12, b=1)
    v2 = func(a=12, b=1)
    assert v1 is v2


def test_cache_mix():
    v1 = func(12, 1)
    val_1 = func(a=12, b=1)
    v2 = func(12, 1)
    val_2 = func(a=12, b=1)
    assert v1 is v2
    assert val_1 is val_2

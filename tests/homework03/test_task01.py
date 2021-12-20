from homework03.task01.task01 import cache


def test_cache():
    calls_counter = 0

    @cache(times=2)
    def func(a, b):
        nonlocal calls_counter
        calls_counter += 1
        return a + b + calls_counter

    assert func(12, b=2) == 15
    assert func(12, b=2) == 15
    assert func(12, b=2) == 15
    assert not func(12, b=2) == 15
    assert func(12, b=2) == 16
    assert func(12, b=2) == 16
    assert func(12, b=2) == 17

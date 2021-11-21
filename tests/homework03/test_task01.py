from homework03.task01.task01 import cache

GLOBAL = 0


def test_cache():
    @cache(times=2)
    def func(a, b):
        global GLOBAL
        GLOBAL += 1
        return a + b + GLOBAL

    assert func(12, b=2) == 15
    assert func(12, b=2) == 15
    assert func(12, b=2) == 15
    assert not func(12, b=2) == 15
    assert func(12, b=2) == 16
    assert func(12, b=2) == 16
    assert func(12, b=2) == 17

"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.


def func(a, b):
    return (a ** b) ** 2


cache_func = cache(func)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)

assert val_1 is val_2

"""
from typing import Callable


class Cache(object):
    def __init__(self):
        self.keys = []
        self.values = []


def cache(func: Callable) -> Callable:
    cache = Cache()

    def wraper(*args, **kwargs):
        nonlocal cache
        try:
            key = cache.keys.index((args, kwargs))
            result = cache.values[key]
        except ValueError:
            result = func(*args, **kwargs)
            cache.keys.append((args, kwargs))
            cache.values.append(result)
        return result

    return wraper

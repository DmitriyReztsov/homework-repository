from typing import Callable


class Cache(object):
    def __init__(self):
        self.keys = []
        self.values = []


def cache(times: int):
    cache = Cache()

    def cache_wraper(func: Callable):
        remaind = times

        def wraper(*args, **kwargs):
            nonlocal cache
            nonlocal remaind
            try:
                if remaind == 0:
                    key = cache.keys.index((args, kwargs))
                    cache.keys.pop(key)
                    cache.values.pop(key)
                    remaind = times
                key = cache.keys.index((args, kwargs))
                result = cache.values[key]
                remaind -= 1
            except ValueError:
                result = func(*args, **kwargs)
                cache.keys.append((args, kwargs))
                cache.values.append(result)
            return result

        return wraper

    return cache_wraper

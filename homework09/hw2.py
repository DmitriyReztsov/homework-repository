"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.

>>> with supressor(IndexError):
...    [][2]

"""
from contextlib import contextmanager


class SupressorCls:
    def __init__(self, ignore_error):
        self.ignore = ignore_error
        pass

    def __enter__(self):
        pass

    def __exit__(self, error_type, error_value, error_traceback):
        return isinstance(error_value, self.ignore)


@contextmanager
def supressor_gen(ignore_error):
    try:
        yield
    except ignore_error:
        pass

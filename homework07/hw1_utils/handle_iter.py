from homework07.hw1_utils import EASY_ITER_TYPE, PURE_TYPE
from homework07.hw1_utils import handle_dict as hd


def handle_iter(iterable, element):
    counter = 0
    for value in iterable:
        if isinstance(value, tuple(val for val in PURE_TYPE)):
            counter = (
                counter + 1
                if value == element and type(value) == type(element)
                else counter
            )
        if isinstance(value, tuple(val for val in EASY_ITER_TYPE)):
            counter += handle_iter(value, element)
        if isinstance(value, dict):
            counter += hd.handle_dict(value, element)
    return counter

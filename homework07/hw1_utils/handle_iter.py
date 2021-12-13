from hw1_utils import EasyIterType, PureType
from hw1_utils import handle_dict as hd


def handle_iter(iterable, element):
    counter = 0
    for value in iterable:
        if isinstance(value, tuple(val.value for val in PureType)):
            counter = (
                counter + 1
                if value == element and type(value) == type(element)
                else counter
            )
        if isinstance(value, tuple(val.value for val in EasyIterType)):
            counter += handle_iter(value, element)
        if isinstance(value, dict):
            counter += hd.handle_dict(value, element)
    return counter

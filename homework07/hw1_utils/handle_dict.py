from homework07.hw1_utils import EASY_ITER_TYPE, PURE_TYPE
from homework07.hw1_utils import handle_iter as hi


def handle_dict(t_dict, element):
    counter = 0
    for key, value in t_dict.items():
        if key == element:
            counter += 1
        if isinstance(value, tuple(val for val in PURE_TYPE)):
            counter = (
                counter + 1
                if value == element and type(value) == type(element)
                else counter
            )
        if isinstance(value, tuple(val for val in EASY_ITER_TYPE)):
            counter += hi.handle_iter(value, element)
        if isinstance(value, dict):
            counter += handle_dict(value, element)
    return counter

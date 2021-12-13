from hw1_utils import EasyIterType, PureType
from hw1_utils import handle_iter as hi


def handle_dict(t_dict, element):
    counter = 0
    for key, value in t_dict.items():
        if key == element:
            counter += 1
        if isinstance(value, tuple(val.value for val in PureType)):
            counter = (
                counter + 1
                if value == element and type(value) == type(element)
                else counter
            )
        if isinstance(value, tuple(val.value for val in EasyIterType)):
            counter += hi.handle_iter(value, element)
        if isinstance(value, dict):
            counter += handle_dict(value, element)
    return counter

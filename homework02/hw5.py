"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""


class CustomError(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr(self.data)


def validate_data(iterable, *args):
    """Data should be validated. Input should consist of:
    1. iterable object;
    2. Values of start and stop - the same type as data in iterable
    3. Step - type int.

    """
    try:
        _ = iter(iterable)
    except TypeError:
        print("ERROR : Function expected iterable object as first argument !")
        raise SystemExit

    try:
        if len(args) == 0:
            raise CustomError(
                "ValueError : not enough values to unpack (expected 3, got 0)"
            )
    except CustomError as er:
        print(f"ERROR : {er.data}")
        raise SystemExit

    if len(args) == 1:
        start, stop, step = None, *args, 1
    elif len(args) == 2:
        start, stop, step = *args, 1
    elif len(args) == 3:
        start, stop, step = args
    else:
        print("ValueError : too many values to unpack (expected 3) !")
        raise SystemExit

    try:
        if start and not start in iterable:
            raise CustomError("Start is not in range !")
        if not stop in iterable:
            raise CustomError("Stop is not in range !")
        if not isinstance(step, int):
            raise CustomError(
                (f"Type of step arg should be int, " f"{type(step)} passed !")
            )
    except CustomError as er:
        print(f"ERROR: {er.data}")
        raise SystemExit
    except TypeError:
        print(
            "TypeError : data type in iterable doesn't correspond with passed argument !"
        )
        raise SystemExit
    return start, stop, step


def custom_range(iterable, *args):
    """Function recieves iterables and positional arguments only.
    In case of input dictionary, function returns list of tuples with key and value.
    This behavior wasn't described in the conditions, so it was my decision.

    """
    start, stop, step = validate_data(iterable, *args)
    result = []
    if step < 0:
        iterator = reversed(iterable)
    else:
        iterator = iter(iterable)
    i = 0
    stop_activated = False
    start_activated = False if start else True
    while True:
        try:
            value = next(iterator)
        except StopIteration:
            break
        if value == stop:
            stop_activated = True
        if value == start:
            start_activated = True
        if i % step == 0 and start_activated == True and stop_activated == False:
            if not isinstance(iterable, dict):
                result.append(value)
            else:
                result.append((value, iterable[value]))
        i += 1
    return result

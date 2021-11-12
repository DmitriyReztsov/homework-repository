"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers,
    and returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    data_to_process = list(data)
    assert (
        len(data_to_process) >= 3
    ), "The check needs at least 3 integers in sequence !"
    a, b, c = data_to_process[0], data_to_process[1], data_to_process[2]

    if a < 0 or b < 0:
        return False

    while len(data_to_process) >= 3:
        if (a + b) != c:
            return False

        data_to_process = data_to_process[1:]
        if len(data_to_process) >= 3:
            a, b, c = b, c, data_to_process[2]

    return True

"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers,
    and returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import Sequence


def generator_fibonacci(start=0, stop=0):
    first = 0
    second = 1
    while first < start:
        first, second = second, (first + second)
    while first < stop:
        yield first
        first, second = second, (first + second)
    yield first


def check_fibonacci(data: Sequence[int]) -> bool:
    data_to_process = list(data)
    if len(data_to_process) < 3:
        print("The check needs at least 3 integers in sequence !")
        return False
    if data_to_process[0] < 0:
        return False

    fibonacci_list = [
        i for i in generator_fibonacci(data_to_process[0], data_to_process[-1])
    ]
    if data_to_process[0] == 1 and data_to_process[1] != 1:
        fibonacci_list.pop(0)
    return data_to_process == fibonacci_list

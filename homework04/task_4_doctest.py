"""
Write a function that takes a number N as an input and returns N FizzBuzz
numbers*
Write a doctest for that function.

Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - doctests are run with pytest command

You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests


assert fizzbuzz(5) == ["1", "2", "fizz", "4", "buzz"]

* https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15, "Робот Фортран, чисть
картошку!"

This is function FuzzBuzz.

for example,

>>> fizzbuzz(15)
['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', \
'11', 'fizz', '13', '14', 'fizzbuzz']

"""

from typing import List


def fizzbuzz(n: int) -> List[str]:
    """ Returns list of numbers as strings, any number divisible by three is
    replaced by the word fizz
    and any number divisible by five by the word buzz.
    Numbers divisible by 15 become fizzbuzz

    >>> fizzbuzz(30)
    ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', \
'fizz', '13', '14', 'fizzbuzz', '16', '17', 'fizz', '19', 'buzz', 'fizz', \
'22', '23', 'fizz', 'buzz', '26', 'fizz', '28', '29', 'fizzbuzz']

    >>> fizzbuzz(-30)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0

    >>> fizzbuzz(3.0)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer
    """
    if not n >= 0:
        raise ValueError("n must be >= 0")
    if not isinstance(n, int):
        raise ValueError("n must be exact integer")
    result = []
    for i in range(1, n + 1):
        flag = True
        fb_value = ""
        if i % 3 == 0:
            fb_value += "fizz"
            flag = False
        if i % 5 == 0:
            fb_value += "buzz"
            flag = False
        if flag:
            fb_value = str(i)
        result.append(fb_value)
    return result

"""
Armstrong number is a number that is the sum of its own digits each raised
to the power of the number of digits.
https://en.wikipedia.org/wiki/Narcissistic_number

Examples:

- 9 is an Armstrong number, 9 = 9^1 = 9
- 10 is not: 10 != 1^2 + 0^2 = 1
- 153 is : 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153


Write a function that detects if a number is Armstrong number
in functionaly style:
 - use map or other utilities from functools library,
 - use anonymous functions (or use function as argument)
 - do not use loops, preferably using list comprehensions

### Example function signature and call
"""


def is_armstrong(number: int) -> bool:
    if number > 0:
        digits = len(str(number))
        list = [
            ((number // (10 ** i) - (number // (10 ** (i + 1)) * 10))) ** digits
            for i in range(digits)
        ]
        return sum(list) == number
    return False


def is_armstrong_2(number: int) -> bool:
    if number > 0:
        digits = [int(d) for d in str(number)]
        powered_digits = list(map(lambda _: _ ** len(digits), digits))
        return sum(powered_digits) == number
    return False


assert is_armstrong(153) is True, "Is Armstrong number"
assert is_armstrong(10) is False, "Is not Armstrong number"

"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".

    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".

    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".

"""


def parsing_editor(string: str) -> str:
    del_char = 0
    result = []
    for char in reversed(string):
        if char == "#":
            del_char += 1
            continue
        if del_char == 0:
            result.append(char)
        del_char -= 1 if del_char > 0 else del_char
    return "".join(reversed(result))


def backspace_compare(first: str, second: str):
    return parsing_editor(first) == parsing_editor(second)

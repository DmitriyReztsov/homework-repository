"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import re
import unicodedata
from collections import defaultdict
from typing import List, NamedTuple


def get_longest_diverse_words(file_path: str) -> List[str]:
    class Word(NamedTuple):
        word: str
        len_word: int
        amount_uniq: int

    def add_to_list(line_from_file, result):
        words = re.findall(r"[\w']+", line_from_file)
        # регуляка ищет последовательность букв, цифр, <_> и апострофов
        # \w - буквы, цифры и нижние подчеркивания, <'> - плюс апостроф
        # [] - любой символ из перечисленных (см. строкой выше)
        # + - последовательность любой длины из таких символов
        for word in words:
            w = Word(word, len(word), len(set(word)))
            result.append(w)
        return result

    with open(file_path, encoding="unicode_escape", errors="ignore") as f:
        result = []
        while True:
            line_from_file = f.readline()
            if not line_from_file:
                break
            result = add_to_list(line_from_file, result)
        result.sort(reverse=True, key=lambda w: w.amount_uniq)
        result.sort(reverse=True, key=lambda w: w.len_word)
        result_words = [word.word for word in result[:10]]
    return result_words


def get_rarest_char(file_path: str) -> str:
    with open(file_path, encoding="unicode_escape") as f:
        result = defaultdict(int)
        while True:
            char = f.read(1)
            if not char:
                break
            """if char.isspace():
                continue"""
            if char.isalnum():  # отбрасывает символы пунктуации
                result[char] += 1
    return sorted(result, key=result.get)[0]


def count_punctuation_chars(file_path: str) -> int:
    with open(file_path, encoding="unicode_escape") as f:
        result = 0
        while True:
            char = f.read(1)
            if not char:
                break
            if unicodedata.category(char).startswith("P"):
                result += 1
    return result


def count_non_ascii_chars(file_path: str) -> int:
    with open(file_path, encoding="unicode_escape") as f:
        result = 0
        while True:
            char = f.read(1)
            if not char:
                break
            result = (result + 1) if not char.isascii() else result
    return result


def get_most_common_non_ascii_char(file_path: str) -> str:
    with open(file_path, encoding="unicode_escape") as f:
        result = defaultdict(int)
        while True:
            char = f.read(1)
            if not char:
                break
            if char.isascii():
                continue
            result[char] += 1
    return sorted(result, key=result.get)[-1]

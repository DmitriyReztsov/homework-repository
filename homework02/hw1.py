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
from typing import List, NamedTuple


def get_longest_diverse_words(file_path: str) -> List[str]:
    class Word(NamedTuple):
        word: str
        len_word: int
        amount_uniq: int

    def add_to_list(file, result):
        words = re.findall(r"[\w']+", file)
        for word in words:
            w = Word(word, len(word), len(set(word)))
            result.append(w)
        return result

    with open(file_path, encoding="unicode_escape", errors="ignore") as f:
        result = []
        while True:
            file = f.readline()
            if not file:
                break
            result = add_to_list(file, result)
        result.sort(reverse=True, key=lambda w: w.amount_uniq)
        result.sort(reverse=True, key=lambda w: w.len_word)
        result_words = [word.word for word in result[:10]]
    return result_words


def get_rarest_char(file_path: str) -> str:
    with open(file_path, encoding="unicode_escape") as f:
        result = {}
        while True:
            char = f.read(1)
            if not char:
                break
            if char.isspace():
                continue
            try:
                result[char] += 1
            except:
                result[char] = 1
    return sorted(result, key=result.get)[0]


def count_punctuation_chars(file_path: str) -> int:
    with open(file_path, encoding="unicode_escape") as f:
        result = 0
        while True:
            char = f.read(1)
            if not char:
                break
            result = (
                (result + 1) if unicodedata.category(char).startswith("P") else result
            )
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
        result = {}
        while True:
            char = f.read(1)
            if not char:
                break
            if char.isascii():
                continue
            try:
                result[char] += 1
            except:
                result[char] = 1
    return sorted(result, key=result.get)[-1]

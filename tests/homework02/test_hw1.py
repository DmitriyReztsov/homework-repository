from unittest import mock

from homework02.hw1 import (
    count_non_ascii_chars,
    count_punctuation_chars,
    get_longest_diverse_words,
    get_most_common_non_ascii_char,
    get_rarest_char,
)


def test_get_longest_diverse_words(open_file):
    with mock.patch("builtins.open", open_file):
        result = get_longest_diverse_words("file_name")
    assert len(result) == 10
    assert result[0] == "qwertyuiop"


def test_get_rarest_char(open_file):
    with mock.patch("builtins.open", open_file):
        result = get_rarest_char("file_name")
    assert result == "\u2014"


def test_count_punctuation_chars(open_file):
    with mock.patch("builtins.open", open_file):
        result = count_punctuation_chars("file_name")
    assert result == 4


def test_count_non_ascii_chars(open_file):
    with mock.patch("builtins.open", open_file):
        result = count_non_ascii_chars("file_name")
    assert result == 3


def test_get_most_common_non_ascii_char(open_file):
    with mock.patch("builtins.open", open_file):
        result = get_most_common_non_ascii_char("file_name")
    assert result == "\u00e4"

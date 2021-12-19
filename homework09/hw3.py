"""
Write a function that takes directory path, a file extension and an optional
tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.

For dir with two files from hw1.py:
>>> universal_file_counter(test_dir, "txt")
6
>>> universal_file_counter(test_dir, "txt", str.split)
6

"""
import os
from pathlib import Path
from typing import Callable, Optional


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    files_in_dir = list(
        entry
        for entry in os.scandir(dir_path)
        if entry.is_file() and entry.name.endswith(file_extension)
    )
    count = 0
    for file in files_in_dir:
        with open(file.path) as current_file:
            red_data = current_file.read()
            objects_in_file = (
                red_data.split("\n") if not tokenizer else tokenizer(red_data)
            )
            count += len(objects_in_file)
    return count

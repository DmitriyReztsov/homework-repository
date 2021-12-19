"""
Write a function that merges integer from sorted files and returns an iterator

file1.txt:
1
3
5

file2.txt:
2
4
6

>>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
import itertools


class CustomIterator:
    def __init__(self, iterable) -> None:
        self.data_row = iterable
        self.cursor = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.cursor += 1
        if len(self.data_row) > self.cursor:
            return self.data_row[self.cursor]
        raise StopIteration


def validate_data(input_data):
    for entry in input_data:
        try:
            int(entry)
        except ValueError:
            raise ValueError("Check you data: no chars, no empty lines, no spaces")


def merge_sorted_files(file_list):
    data_row = []
    for file in file_list:
        with open(file) as data_file:
            data_from_file = data_file.read().split("\n")
            validate_data(data_from_file)
            data_row.append(data_from_file)
    data_row_joined = list(itertools.chain.from_iterable(data_row))
    data_row_int = list(map(int, data_row_joined))
    data_row_int.sort()
    return CustomIterator(data_row_int)

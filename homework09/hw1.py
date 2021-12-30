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


def merge_sort(array_1, array_2):
    sorted_array = []
    index_1 = 0
    index_2 = 0
    while index_1 < len(array_1) and index_2 < len(array_2):
        if int(array_1[index_1]) < int(array_2[index_2]):
            insert_element = int(array_1[index_1])
            index_1 += 1
        elif int(array_1[index_1]) >= int(array_2[index_2]):
            insert_element = int(array_2[index_2])
            index_2 += 1
        sorted_array.append(insert_element)
    if index_1 < len(array_1):
        sorted_array.extend(array_1[index_1:])
    elif index_2 < len(array_2):
        sorted_array.extend(array_2[index_2:])
    return sorted_array


def merge_sorted_files(file_list):
    data_row = []
    for file in file_list:
        with open(file) as data_file:
            data_from_file = data_file.readlines()
            data_row = merge_sort(data_row, data_from_file)
    data_row_int = list(map(int, data_row))
    return CustomIterator(data_row_int)

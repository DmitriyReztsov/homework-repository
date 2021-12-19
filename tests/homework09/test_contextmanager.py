import os
from contextlib import contextmanager


@contextmanager
def create_files(texts):
    files = []
    try:
        for index, text in enumerate(texts):
            file = os.path.abspath(f"tests/homework09/test_file_{index}.txt")
            fd = open(file, "w", encoding="utf8")
            fd.write(text)
            fd.close()
            files.append(file)
        yield files
    finally:
        for file in files:
            os.remove(file)

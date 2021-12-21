import os
from contextlib import contextmanager


@contextmanager
def create_files(texts):
    files = []
    test_dir = os.path.abspath(f"tests/homework09/test_dir")
    try:
        for index, text in enumerate(texts):
            file = os.path.abspath(f"tests/homework09/test_file_{index}.txt")
            fd = open(file, "w", encoding="utf8")
            fd.write(text)
            fd.close()
            files.append(file)
        if not os.path.exists(test_dir):
            os.makedirs(test_dir)
        file_dir = os.path.abspath(f"tests/homework09/test_dir/test_file_dir.txt")
        fd = open(file_dir, "w", encoding="utf8")
        fd.write("1")
        fd.close()
        files.append(file_dir)
        yield files
    finally:
        for file in files:
            os.remove(file)
        os.removedirs(test_dir)

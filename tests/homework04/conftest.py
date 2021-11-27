import os

from pytest import fixture

TEXT_TRUE = "1"

TEXT_FALSE = "5"

TEXT_ERROR = "a s"


@fixture()
def create_file_True(tmpdir):
    file_True = os.path.abspath("tests/homework04/text_with_number_True.txt")
    fd = open(file_True, "w", encoding="utf8")
    fd.write(TEXT_TRUE)
    fd.close()
    yield file_True
    os.remove(file_True)


@fixture()
def create_file_False(tmpdir):
    file_False = os.path.abspath("tests/homework04/text_with_number_False.txt")
    fd = open(file_False, "w", encoding="utf8")
    fd.write(TEXT_FALSE)
    fd.close()
    yield file_False
    os.remove(file_False)


@fixture()
def create_file_Error(tmpdir):
    file_Error = os.path.abspath("tests/homework04/text_with_number_Error.txt")
    fd = open(file_Error, "w", encoding="utf8")
    fd.write(TEXT_ERROR)
    fd.close()
    yield file_Error
    os.remove(file_Error)

import os
import sqlite3
from unittest import mock

from pytest import fixture

TEXT_1 = "name=kek\n" "last_name=top\n" "power=9001\n" "song=1001\n"

TEST_DB_DATA = [
    ("1", "Ivan", "18", "Moscow", "sunny"),
    ("2", "Marya", "28", "Saint-Petersburg", "nasty"),
    ("3", "Peter", "23", "Pskov", "windy"),
    ("4", "Ivan Ivonovich", "15", "Moscow", "sunny"),
    ("5", "Ivanov Ivan Ivanovich", "68", "Novgorod", "cloudy"),
]


@fixture()
def open_file():
    read_data = TEXT_1
    return mock.mock_open(read_data=read_data)


@fixture()
def open_file_err():
    read_data = "1=TEXT_1"
    return mock.mock_open(read_data=read_data)


@fixture()
def create_db():
    path_to_db = os.path.abspath("tests/homework08/test.sqlite")
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS test_example(
        id INT PRIMARY KEY,
        name TEXT,
        age INT,
        city TEXT,
        weather TEXT);
    """
    )
    connection.commit

    with connection:
        cursor.executemany(
            "INSERT INTO test_example VALUES(?, ?, ?, ?, ?);", TEST_DB_DATA
        )

    connection.close()
    yield path_to_db
    os.remove(path_to_db)

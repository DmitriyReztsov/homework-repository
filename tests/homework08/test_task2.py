import pytest

from homework08.task2 import TableData

test_data = [
    ("Ivan", [(1, "Ivan", 18, "Moscow", "sunny")]),
    ("Marya", [(2, "Marya", 28, "Saint-Petersburg", "nasty")]),
    ("Peter", [(3, "Peter", 23, "Pskov", "windy")]),
    ("Ivan Ivonovich", [(4, "Ivan Ivonovich", 15, "Moscow", "sunny")]),
    ("Ivanov Ivan Ivanovich", [(5, "Ivanov Ivan Ivanovich", 68, "Novgorod", "cloudy")]),
]


def test_db(create_db):
    path_to_bd = create_db
    data_from_db = TableData(database=path_to_bd, table="test_example")
    assert len(data_from_db) == 5


@pytest.mark.parametrize("test_input, expected", test_data)
def test_db_as_dict(create_db, test_input, expected):
    path_to_bd = create_db
    data_from_db = TableData(database=path_to_bd, table="test_example")
    assert data_from_db[test_input] == expected

    true_statement = test_input in data_from_db
    false_statement = "Yeltsin" in data_from_db
    assert true_statement is True
    assert false_statement is False


def test_iteration(create_db):
    path_to_bd = create_db
    data_from_db = TableData(database=path_to_bd, table="test_example")
    cities = ["Moscow", "Saint-Petersburg", "Pskov", "Moscow", "Novgorod"]
    for index, person in enumerate(data_from_db):
        assert person["city"] == cities[index]

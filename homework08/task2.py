import re
import sqlite3
from contextlib import contextmanager


@contextmanager
def open_db(database):
    try:
        connection = sqlite3.connect(database)
        yield connection.cursor()
    finally:
        connection.close()


class TableData:
    def __init__(self, database, table):
        if not TableData.validate_input(database, table):
            raise ValueError("wrong values")
        self.database = database
        self.table = table

    def __len__(self):
        len = 0
        with open_db(self.database) as cursor:
            cursor.execute(f"SELECT * FROM {self.table}")
            while cursor.fetchone():
                len += 1
        return len

    def __getitem__(self, key):
        with open_db(self.database) as cursor:
            cursor.execute(
                f"SELECT * FROM {self.table} WHERE name=:name", {"name": key}
            )
            data = cursor.fetchall()
        return data

    def __contains__(self, lookup):
        with open_db(self.database) as cursor:
            cursor.execute(
                f"SELECT * FROM {self.table} WHERE name=:name", {"name": lookup}
            )
            data = cursor.fetchall()
        return bool(data)

    def generator(self):
        with open_db(self.database) as cursor:
            cursor.execute(f"SELECT * FROM {self.table}")
            column_names = [description[0] for description in cursor.description]
            while row := cursor.fetchone():
                data_dict = dict(zip(column_names, row))
                yield data_dict

    def __iter__(self):
        return self.generator()

    @staticmethod
    def validate_input(database, table):
        database_mask = r"[\w/.]+"  # # 0-9, Aa-Zz, _, /
        table_mask = r"[\w]+"  # 0-9, Aa-Zz, _
        if re.match(database_mask, database) and re.match(table_mask, table):
            return True
        return False

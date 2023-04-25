"""
Модуль описывает репозиторий, работающий в sqlite
"""

import sqlite3
from typing import Generic, TypeVar, Protocol, Any
from inspect import get_annotations

T = TypeVar('T')


class SqliteRepository(Generic[T]):
    """
    Репозиторий, работающий в sqlite. Хранит данные в БД.
    """

    def __init__(self, db_file: str, cls: type) -> None:
        self.db_file = db_file
        self.table_name = cls.__name__.lower()
        self.fields = get_annotations(cls, eval_str=True)
        self.type = cls

    def add(self, obj: T):
        names = ', '.join(self.fields.keys())
        placeholders = ', '.join("?" * len(self.fields))
        values = [getattr(obj, x) for x in self.fields]
        with sqlite3.connect(self.db_file) as con:
            cur = con.cursor()
            cur.execute('PRAGMA foreign_keys = ON')
            cur.execute(
                f'INSERT INTO {self.table_name} ({names}) VALUES ({placeholders})',
                values
            )
        con.close()

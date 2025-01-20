import sqlite3
from contextlib import contextmanager
from pathlib import Path

path_to_database = Path(__file__).parent.parent / 'sql_lite_edit'

@contextmanager
def create_connection(db_file):
    """creating a database connection to a SQLite database"""
    conn = sqlite3.connect(db_file)
    yield conn
    conn.rollback()
    conn.close()

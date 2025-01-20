import sqlite3
from contextlib import contextmanager
from pathlib import Path
from  datetime import datetime
from datetime import date

path_to_database = Path(__file__).parent / 'salary.db'

def adapt_date_iso(val:date):
    """преобразует datetime.date в строку формата ISO 8601 (год-месяц-день)"""
    return val.isoformat()

def addapt_datetime_iso(val:date):
    """преобразет datetime.date в строку ISO 8601 (год-месяц-день-час-минута-секунда)"""
    return val.isoformat()

def convert_date(val:bytes):
    """преобразует строку ISO 8601 в формат datetime.datetime"""
    return date.fromisoformat(val.decode())

def convert_datetime(val:bytes):
    """преобразует строку ISO 8601 в формат datetime.datetime"""
    return datetime.fromisoformat(val.decode())

sqlite3.register_adapter(date, adapt_date_iso)
sqlite3.register_adapter(datetime, addapt_datetime_iso)

sqlite3.register_converter('date', convert_date)
sqlite3.register_converter('datetime', convert_datetime)


@contextmanager
def create_connection(db_file):
    """creating a database connection to a SQLite database"""
    conn = None
    try:
        conn = sqlite3.connect(
            db_file,
            detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES
            )
        yield conn
    except sqlite3.Error as e:
        print('Error data base', e)
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()

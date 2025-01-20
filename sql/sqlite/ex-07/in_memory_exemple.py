import sqlite3
from contextlib import contextmanager
from sqlite3 import Error
path_to_database = ':memory:'
@contextmanager
def transaction(db_file):
    """creating connection"""

    conn = sqlite3.connect(db_file)
    try:
        yield conn
        conn.commit()
    except Error as e:
        conn.rollback()
        raise e
    finally:
        conn.close()


if __name__ == '__main__':
    with transaction(path_to_database) as conn:
        if conn is not None:
            writer = conn.cursor()
            reader = conn.cursor()

            writer.execute('create table movie(title, year, score)')

            data = [
                ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
                ("Monty Python's The Meaning of Life", 1983, 7.5),
                ("Monty Python's Life of Brian", 1979, 8.0),
            ]

            reader.executemany('insert into movie values(?,?,?)', data)

            reader.execute('select * from movie')

            # print(cursor.fetchall())
            for row in reader.execute('select year, title from movie order by year'):
                print(row)


from sqlite3 import Error, Connection
from sql.sqlite.connect import create_connection, path_to_database

def delete_task(conn:Connection, id:int):
    """
    Delete a task by task id
    :param conn:  Connection to the SQLite database
    :param id: id of the task
    :return:
    """
    sql = 'DELETE FROM tasks WHERE id=?'
    cur = conn.cursor()
    try:
        cur.execute(sql, (id,))
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cur.close()


if __name__ == '__main__':
    with create_connection(path_to_database) as conn:
        delete_task(conn, 1)

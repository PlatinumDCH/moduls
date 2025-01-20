from sqlite3 import Error, Connection
from connect import create_connection, path_to_database

def select_projects(conn:Connection)->None| list[tuple]:
    rows = None
    cur = conn.cursor()
    try:
        cur.execute('select * from projects')
        rows = cur.fetchall()
    except Error as e:
        print(e)
    finally:
        cur.close()
    return rows

def select_all_tasks(conn:Connection)->None|list[tuple]:
    rows = None
    cur = conn.cursor()
    try:
        cur.execute('select * from tasks')
        rows = cur.fetchall()
    except Error as e:
        print(e)
    finally:
        cur.close()
    return rows

def select_task_by_status(conn:Connection, status:bool)->None|list[tuple]:
    rows = None
    cur = conn.cursor()
    try:
        cur.execute('select * from tasks where status=?', (status,))
        rows = cur.fetchall()
    except Error as e:
        print(e)
    finally:
        cur.close()
    return rows

if __name__ == '__main__':
    with create_connection(path_to_database) as conn:
        print('Projects:')
        projects = select_projects(conn)
        print(projects)

        print('\nQuery all tasks')
        tasks = select_all_tasks(conn)
        print(tasks)

        print('\nQuery tasks by status:')
        tasks_by_priory = select_task_by_status(conn, True)
        print(tasks_by_priory)


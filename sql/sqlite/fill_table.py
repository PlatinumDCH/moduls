from sqlite3 import Error, Connection
from connect import create_connection, path_to_database

def create_project(conn:Connection, project):
    sql = '''
    insert into projects(name, begin_date, end_date)
    values(?, ?, ?);
    '''
    cur = conn.cursor()
    try:
        cur.execute(sql, project)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cur.close()
    return cur.lastrowid

def create_task(conn:Connection, task):
    sql = '''insert into tasks
        (name, priority, status, project_id,begin_date,end_date) 
        VALUES(?,?,?,?,?,?);'''
    
    cur = conn.cursor()
    try:
        cur.execute(sql, task)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cur.close()
    return cur.lastrowid

if __name__ == '__main__':
    with create_connection(path_to_database) as connection:
        #fill table projects
        project = ('Cool App with sqlite and python','2025-01-01','2026-01-01')
        project_id = create_project(connection, project )
        print(project_id)

        #fill table task
        task_1 = ('Analyze the requirements of the app', 1, True, project_id, '2022-01-01', '2022-01-02')
        task_2 = ('Confirm with user about the top requirements', 1, False, project_id, '2022-01-03', '2022-01-05')

        #create task
        print(create_task(connection, task_1))
        print(create_task(connection, task_2))



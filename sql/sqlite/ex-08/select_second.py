from connect import create_connection, path_to_database


def execute_query(sql: str) -> list:
    with create_connection(path_to_database) as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

#количество сотрудников в компании
sql = """
SELECT COUNT(*), c.company_name
FROM employees e
LEFT JOIN companies c ON e.company_id = c.id
GROUP BY c.id;
"""

print(execute_query(sql))
from connect import create_connection, path_to_database



def execute_query(sql: str) -> list:
    with create_connection(path_to_database) as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


# выбрать всех работников которые на протяжении 7 месяцев получали больше 5000
sql = """
SELECT comp.company_name, emp.employees, emp.post, pay.total
FROM companies comp
    LEFT JOIN employees emp ON emp.company_id = comp.id
    LEFT JOIN payments pay ON pay.employee_id = emp.id
WHERE pay.total > 5000
    AND  pay.date_of BETWEEN  '2021-07-10' AND  '2021-07-20'
"""

print(execute_query(sql))

from connect import create_connection, path_to_database

def execute_query(sql:str)->list:
    with create_connection(path_to_database) as connection:
        cursor = connection.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

sql = '''
select round(avg(pay.total), 2), emp.post
from payments as pay
left join employees as emp on pay.employee_id = emp.id
group by emp.post'''

print(execute_query(sql))

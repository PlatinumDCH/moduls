import pathlib
from connect import create_connection, path_to_database

path_sql = pathlib.Path(__file__).parent / 'salary.sql'
def create_db():
    #чтение файла с скриптом для создания таблиц из бд
    with create_connection(path_to_database) as conn:
        with open(path_sql, 'r', encoding='unf-8') as file:
            sql = file.read()
        
        cursor = conn.cursor()
        cursor.executescript(sql)
        print('Table sucesfull created')

if __name__ == '__main__':
    create_db()
    

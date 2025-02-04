import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="test_db"
)

create_tables = '''create table genders(
    id int primary key, -- уникальный ключ обьектов таблицы
    name varchar(30), -- название гендера 
    created_at timestamp default CURRENT_TIMESTAMP -- когда был создан
);
'''
cursor = conn.cursor()
cursor.execute(create_tables)
cursor.execute("SHOW TABLES;")
print(cursor.fetchall())

conn.close()

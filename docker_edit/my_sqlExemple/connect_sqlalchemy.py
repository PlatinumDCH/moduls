from sqlalchemy import create_engine, text

# Создаем подключение к MySQL
engine = create_engine("mysql+pymysql://root:root@127.0.0.1:3306/test_db")


query = text("SHOW TABLES;")

# Проверяем подключение
with engine.connect() as conn:
    result = conn.execute(query)
    print(result.fetchone())  # Должно вывести ('test_db',)

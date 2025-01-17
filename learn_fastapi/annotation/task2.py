import sqlite3
from typing import Callable, get_type_hints, get_origin, Annotated
from functools import wraps

class Injectable:
    """
    используеться для описания зависимостей
    хранит ссылку и на функцию или обьект, который возвращает зависимость
    """
    def __init__(self, dependency) -> None:
        self.dependency = dependency


def inject(func: Callable) -> Callable:
    """
    автоматически определить зависимость, указанные в аннотациях и подставить
    их в аргументы функции
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        get_type_hints - для извлечения аннотация параметров функции
        get_origin, Annotated - для проверки наличия метаданных
        __metadata__[0] - для получения зависимости их аннотации

        Если аргумент не передан при вызове, декоратор автоматически вызывает 
        указанную зависимость и подставляет её результат
        """
        type_hints = get_type_hints(func, include_extras=True)
        print(f"Type hints for {func.__name__}: {type_hints}")
        injected_kwargs = {}

        for arg, hint in type_hints.items():
            if get_origin(hint) is Annotated and isinstance(hint.__metadata__[0], Injectable):
                dependency = hint.__metadata__[0].dependency
                print(f"Resolving dependency for {arg}: {dependency.__name__}")

                # Рекурсивное разрешение вложенных зависимостей
                resolved_dependency = inject(dependency)
                
                if arg not in kwargs:
                    injected_kwargs[arg] = resolved_dependency()
                    print(f"Injected {arg}: {injected_kwargs[arg]}")

        kwargs.update(injected_kwargs)
        result = func(*args, **kwargs)
        print(f'Result from {func.__name__}: {result}')
        return result
    
    return wrapper

def get_db_config_file_path():
    """ Функция возвращает путь до файла с конфигурацией БД """
    return 'db.config'

def get_db_connect_string(
        file_path: Annotated[str, Injectable(get_db_config_file_path)]
    ) -> str:
    """ Функция возвращает строку для соединения с БД """
    return f'sqlite:///{file_path}'

@inject
def execute_query(
        query: str,
        db_connect_string: Annotated[str, Injectable(get_db_connect_string)]
    ):
    """ выполняет запрос к БД"""
    print(f"Connecting to DB with: {db_connect_string}")

    with sqlite3.connect(":memory:") as conn:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE test (id INTEGER, value TEXT)")
        cursor.execute("INSERT INTO test (id, value) VALUES (1, 'hello')")
        cursor.execute(query)
        return cursor.fetchall()
    
query_result = execute_query("SELECT * FROM test")
print(query_result)
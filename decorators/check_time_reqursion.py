import time
from functools import wraps

def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not hasattr(wrapper, "active"):  # Проверяем, запущен ли замер
            wrapper.active = False

        if not wrapper.active:  # Если замер еще не начался
            wrapper.active = True
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            wrapper.active = False
            print(f"Execution time: {end_time - start_time:.4f} seconds")
            return result
        else:  # Если замер уже идет, просто вызываем функцию
            return func(*args, **kwargs)

    return wrapper



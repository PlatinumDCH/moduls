

def log(prefix):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"{prefix} Вызов {func.__name__} с аргументами {args}, {kwargs}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log("DEBUG:")
def add(a, b):
    return a + b

print(add(2, 3))


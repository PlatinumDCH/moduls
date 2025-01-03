from functools import wraps

def restrict_args_type(typed_args):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not all(isinstance(arg, typed_args) for arg in [*args,*kwargs]):
                raise TypeError(f'All arguments must be of type {typed_args.__name__}')
            return func(*args, **kwargs)
        return wrapper
    return decorator

@restrict_args_type(int)
def add(a, b):
    return a + b
print(add(1,2))
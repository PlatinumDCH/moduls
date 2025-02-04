from functools import wraps
from time import perf_counter

def time_logg(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        print(f'{func.__name__}: {perf_counter() - start}')
        return result
    return wrapper

@time_logg
def long_loop(num:int):
    """simple docstring"""
    while num > 0:
        num -= 1

    print('original function')

if __name__ == '__main__':
    
    long_loop(10_0000)
    print(f'function name: {long_loop.__name__}')
    print(f'doctring function: {long_loop.__doc__}')
    print(f'annotations function: {long_loop.__annotations__}')

    # вызвать задекорированную функцию без декоратора
    # long_loop.__wrapped__(10_0000) 

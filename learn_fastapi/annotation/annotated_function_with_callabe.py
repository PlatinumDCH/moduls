from typing import Callable
from functools import wraps

def smart_divide(func: Callable[[int, int], float]):
    @wraps(func)
    def inner(a:int, b:int):
        if b == 0:
            print('Woops! Division by 0')
            return None
        return func(a, b)
    return inner

@smart_divide
def divide(a:int, b:int)->float:
    result = a / b
    print(a/b)
    return result

 
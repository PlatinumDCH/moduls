import time
from functools import wraps

class RegisterTime:
    def __init__(self, label='Execution Time'):
        self.label = label

    def __call__(self, func):
        @wraps(func) 
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            executed_time = time.time() - start_time
            print(f'{self.label}: {executed_time:.4f} seconds')
            return result
        return wrapper
    
@RegisterTime()
def exemple_function(timer:int):
    time.sleep(timer)
    return 'exemple result'

result_function = exemple_function(5)
print(result_function)
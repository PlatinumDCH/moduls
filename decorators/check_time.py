import time
from functools import wraps

from logger import set_logger

logger = set_logger.main()

class RegisterTime:
    def __init__(self, label='Execution Time'):
        self.label = label

    def __call__(self, func):
        @wraps(func) 
        def wrapper(*args, **kwargs):
            logger.debug('starting meter time')
            start_time = time.time()
            result = func(*args, **kwargs)
            logger.debug('finish meter time')
            executed_time = time.time() - start_time
            print(f'{self.label}: {executed_time:.4f} seconds')
            return result
        return wrapper
    
# @RegisterTime
# def exemple_function(timer:int):
#     time.sleep(timer)
#     return 'exemple result'

# decorated_function= RegisterTime()(exemple_function)
# result_function = decorated_function(1)
# print(result_function)

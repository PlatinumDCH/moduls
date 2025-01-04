import time
from functools import wraps
import redis
from functools import lru_cache


def decor_time(func):
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

redis_client =  redis.StrictRedis(
    host='localhost',
    port=6379,
    db=0,
    decode_responses=True
)

def redis_cache(func):
    @wraps(func)
    def wrapper(*args):
        cache_key = f'{func.__name__}:{args}'

        cached_result = redis_client.get(cache_key)
        if cached_result is not None:
            print(f'Cache hit for {cache_key}')
            return int(cached_result)

            
        print(f'Cache miss for {cache_key}')
        result = func(*args)
        redis_client.set(cache_key, result)
        return result
    return wrapper

@decor_time
@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def fibonacci_iteration (n):
    if n <= 1:
        return n
    a,b = 0,1
    for _ in range(2, n+1):
        a,b = b,a+b
    return b


def fibonacci_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    else:
        value = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
        memo[n] = value
        return value
    
if __name__ == '__main__':
    result = fibonacci(35)
    print(result)
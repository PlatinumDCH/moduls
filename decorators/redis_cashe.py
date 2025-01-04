import time
import redis
from functools import wraps

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

        if (cached_result := redis_client.get(cache_key)) is None:
            print(f'Cache hit for {cache_key}')
            return int(cached_result)
        print(f'Cache miss for {cache_key}')
        result = func(*args)
        redis_client.set(cache_key, result)
        return result
    return wrapper

"""
brew install redis
brew services start redis
redis-cli ping -> PONG

остановить сервис
sudo systemctl stop redi
redis-cli shutdown

"""
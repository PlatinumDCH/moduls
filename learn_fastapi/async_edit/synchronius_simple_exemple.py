import time
import requests
from functools import wraps

url = "https://httpbin.org/get"
def timeDecor(func):
    wraps(func)
    def inner(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print('Time elapsed',end - start )

        return func
    return inner


@timeDecor
def main():
    global url
    r_count = 10
    session = requests.Session()
    for i in range(r_count):
        print(f'making request {i}')
        resp = session.get(url)
        if resp.status_code == 200:
            pass

if __name__ == '__main__':
    main()


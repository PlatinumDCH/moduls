# **Декораторы в Python**
``` 
Декоратор - это функция, которая принимает другую функцию  в качестве аргумунта и добавляет к ней дополнителбную логиук, не изменяя её исходный код 
```
Простой декораторы
``` python
def decotator(func):
    def wrapper():
        # Code to execute BEFORE the original funcion 
        print('before the function call.)

        # Call the original function
        func()

        # Code to execute AFTER the original function
        print('After the function call.')

    return wrapper
```
Если применть этот декоратор к функции:
``` python
@decorator
def foo():
    print('this is orofonal function')

foo()
```
Выход:
``` 
before the function call.
this is orofonal function
After the
```
# Создание и использование декораторов
Базовый декоратор

Вот простой прмер декоратора, который регистрирует вызов функции.
``` python
def logger(func):
    def wrapper(*args, **kwargs):
        print(f'function "{func.__name__}" is being called.')
        result = func(*args, **kwargs)
        print(f"function '{func.__name__}' finished execution.")
        return result
    return wrapper

@logger
def foo(name):
    print(f'Hello {name}')

foo('test')
```
Вывод:
```
function "foo" is being called.
Hello, test
function 'foo' finished execution.
```
## Использование агрументов в декораторах
Декораторы также могут обрабатывать аргументы, переданные обернутой функции, с помощью *args, **kwargs.
``` python
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments {args} and {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@logger
def add(a, b):
    return a + b

result = add(10, 20)
print(f"Result: {result}")
```
Выыод:
```
Calling add with arguments (10, 20) and {}
Result: 30
```
## Цепочка декораторов
К одной функции можно применить несколько декораторов. Они применяются снизу вверх.
``` python
>>> def first_decorator(func):
...     def wrapper():
...         result = func() + ' first decorators '
...         return result
...     return wrapper
... 
>>> def second_decorator(func):
...     def wrapper():
...         result = func() + ' second decorator '
...         return result
...     return wrapper
...
>>> @first_decorator
... @second_decorator
... def foo():
...     return 'test ,'
```
Вывод:
```
test , second decorators  first decotators 
```
##  Декораторы с параметрами
``` python
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("foo!")

greet()
```
Вывод:
```
foo!
foo!
foo!
```
## Встроенные декораторы в Python
- **@staticmethod**
- **@classmethod**
- **@property**

Пример:
``` Python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative.")
        self._radius = value

circle = Circle(5)
print(circle.radius)  # Access property
circle.radius = 10    # Modify property
print(circle.radius)
```
## Практические примеры декораторов:
### Ведение журнала
``` python
def log(func):
    def wrapper(*args, **kwargs):
        print(f"Logging: {func.__name__} was called with arguments {args} and {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log
def divide(a, b):
    return a / b

print(divide(10, 2))
```
### Аутентификация
``` python
def requires_login(func):
    def wrapper(user, *args, **kwargs):
        if not user.get("logged_in"):
            raise PermissionError("User is not logged in!")
        return func(user, *args, **kwargs)
    return wrapper

@requires_login
def view_profile(user):
    print(f"Viewing profile of {user['username']}")

user = {"username": "Abhishek", "logged_in": True}
view_profile(user)
```
### Мониторинг производительности
``` python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)
    print("Function complete!")

slow_function()
```
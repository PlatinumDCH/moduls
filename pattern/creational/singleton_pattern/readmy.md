# Singleton
```
Описание: гарантирует что будет создан только один екземляр класса
```
### Пример в качестве декоратора
``` python
import random

def singleton(class_):
    isinstances_ = {}
    def getinstance(*args, **kwags):
        if class_ not in isinstances_:
            isinstances_[class_] = class_(*args, **kwags)
        return isinstances_[class_]
    return getinstance

@singleton
class Regular:
    def __init__(self, *args, **kwargs):
        self.number = random.randint(1,10)

list_regular = [Regular() for i in range(0, 5)]
for i, el in enumerate(list_regular):
    print(f'element: {i} number: {el.number}')
```
вывод:
```
❯ py decorator_singleton.py
element: 0 number: 10
element: 1 number: 10
element: 2 number: 10
element: 3 number: 10
element: 4 number: 10
```
Без декоратора каждый раз будут выводится ранодомные числа
### Базовый клас
``` python
class Singleton(object):
    _instance = None
    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance
 
class Logger(Singleton):
    pass
```
### Metaclass
```python
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
 
class Logger(metaclass=Singleton):
    pass
```

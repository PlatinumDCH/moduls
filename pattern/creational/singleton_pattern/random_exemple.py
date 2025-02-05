import random

class Simgleton:
    __instance = None

    def __init__(self):
        self.number = random.randint(1,10)

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(Simgleton)
        return cls.__instance

class Regular:
    def __init__(self, *args, **kwargs):
        self.number = random.randint(1,10)
    

def testing():
    print(Simgleton.__name__)
    list_singleton = [Simgleton() for i in range(0, 5)]
    for i, el in enumerate(list_singleton):
        print(f'element: {i} number: {el.number}')

    print()

    print(Regular.__name__)
    list_regular = [Regular() for i in range(0, 5)]
    for i, el in enumerate(list_regular):
        print(f'element: {i} number: {el.number}')

if __name__ == '__main__':
    
    testing()
                           
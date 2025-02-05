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
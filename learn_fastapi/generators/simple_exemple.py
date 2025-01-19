price = [210,300,400,500]

price_iter = price.__iter__()

def simple_printing(iterable_object = price_iter)->None:
    print(iterable_object.__next__()) # 210
    print(iterable_object.__next__()) # 300
    print(iterable_object.__next__()) # 400

    print(price_iter.__next__()) # StopIteration: 

def smart_iterable(iterable_obj = price_iter):
    while True:
        try:
            print(iterable_obj.__next__)
        except StopIteration:
            break
    


def return_10():
    return 10

value = return_10()
print(value) # 10

def return_values():
    yield 1
    yield 2
    yield 'a'

value = return_values()
try:
    print(next(value)) # print(value.__next__())
    print(next(value))
    print(next(value))
    print(next(value))
except StopIteration as e:
    print(f"Out of range , {e}")



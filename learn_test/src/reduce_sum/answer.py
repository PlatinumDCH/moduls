from functools import reduce
numbers = [1, 12, 23, 34, 45, 56, 67, 78, 89, 90]

def other(a):
    print(a)
    return a

def sum_numbers(numbers):
    other('!!TEST!!')
    return reduce(lambda x,y:x+y, numbers)

if __name__ == '__main__':
    print(sum_numbers(numbers))
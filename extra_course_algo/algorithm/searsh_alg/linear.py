import random


def get_arr(
        size_arr:int = 15,
        start:int = 1,
        end:int = 10)->list[int]:
    """
    получить список с заданными характеристикасми

    size_arr - размер массива
    start - начало диапазона
    end - конец диапазона
    """
    return [
        random.randint(start,end)
        for _ in range(size_arr)
        ]

def get_lenght(arr:list):
    return len(arr)

def searsh_element(size:int)->tuple[list,int,int]:
    '''возвращает массив, длину массива, радомный елемент'''
    arr = get_arr(size)
    se_index = random.randint(0, size)
    se = arr[se_index]
    return arr, size, se  


arr, size, se = searsh_element(5)
def linear_search(arr:list, x):
    for i in range(size):
        if arr[i] == x:
            return i
    return -1

def get_index_arr(): #O(n)
    global size
    arr_index = [i for i in range(size)]
    return arr_index
    

def printing(algo):
    """роспечатать подробную информацию"""
    result = algo(arr, se)
    print(f'arr  {arr}')
    print(f'arri {get_index_arr()}')
    print(f'испокмый елмент   {se}')
    print(f'найденный елемент под индексом {result}')

if __name__ == '__main__':
    printing(linear_search)
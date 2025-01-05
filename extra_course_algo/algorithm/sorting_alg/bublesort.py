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
        random.randint(
            start,end
            )
              for _ in range(size_arr)
        ]
    
def get_lenght(arr:list):
    return len(arr)

def bubble_sort(arr:list)->list:
    n = get_lenght(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            values_i_j = i,j
            condition = f'{arr[j]} > {arr[j+1]} {arr[j]>arr[j+1]}'
            if arr[j]>arr[j+1]:
                print(f'processing swap {arr[j]} and {arr[j+1]}')
                arr[j],arr[j+1] = arr[j+1],arr[j]

    return arr

arr = get_arr()

print(arr)
result_list = bubble_sort(arr)
print(result_list)

"""
 
for i in range(n-1):
прходит через весь массив.На каждой итерации елементаы с конца массива
становятся упорядоченными

        for j in range(0, n-i-1):
        

[1, 10, 9, 1, 5, 5, 2, 10, 4, 9, 8, 6, 6, 4, 7]
n = 15

range _i (n - 1) | 14

    range -j(0, n - _i, -1) | 0, 15 - 0 - 1
    frame-1 (0)
        if arr[j] > arr[j+1] 1>10 False
           dont swap | [1, 10, 9, 1, 5, 5, 2, 10, 4, 9, 8, 6, 6, 4, 7]
    frame-2 (1)
        if arr[j] > arr[j+1] 10>9 True
            swap | [1, 9, 10, 1, 5, 5, 2, 10, 4, 9, 8, 6, 6, 4, 7]
    frame-3 (2)
        if arr[j] > arr[j+1] 10>1 True
            swap | [1, 9, 1, 10, 5, 5, 2, 10, 4, 9, 8, 6, 6, 4, 7]
    frame-4 (3)
        if arr[j] > arr[j+1] 10>5 True
            swap | [1, 9, 1, 5, 10, 5, 2, 10, 4, 9, 8, 6, 6, 4, 7]
    frame-5 (4)
        if arr[j] > arr[j+1] 10>5 True
            swap | [1, 9, 1, 5, 5, 10, 2, 10, 4, 9, 8, 6, 6, 4, 7]
    frame-6 (5)
        if arr[j] > arr[j+1] 10>2 True
            swap | [1, 9, 1, 5, 5, 2, 10, 10, 4, 9, 8, 6, 6, 4, 7]
    frame-7 (6)
        if arr[j]>arr[j+1] 10 > 10 false
            dont swap | list not modify
    frame-8 (7)
        if arr[j]>arr[j+1] 10 > 4 True
             swap | [1, 9, 1, 5, 5, 2, 10, 4, 10, 9, 8, 6, 6, 4, 7]
    frame-9 (8)
        if arr[j]>arr[j+1] 10 > 9 True
             swap | [1, 9, 1, 5, 5, 2, 10, 4, 9, 10, 8, 6, 6, 4, 7]
    frame-10 (9)
        if arr[j]>arr[j+1] 10 > 8 True
             swap | [1, 9, 1, 5, 5, 2, 10, 4, 9, 8, 10, 6, 6, 4, 7]
    frame-11,12,13,14
        10>6
        10>6
        10>4
        10>7
    end frame
        [1, 9, 1, 5, 5, 2, 10, 4, 9, 8, 6, 6, 4, 7, 10]

10 больше 
"""
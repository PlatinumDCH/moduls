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


def quick_sort(arr:list)->list:
    n = get_lenght(arr)
    if n <= 1:
        return arr
    
    selected_el = arr[n//2]
    left_part = [
        el 
        for el in arr
        if el < selected_el
    ]
    middle_part = [
        el
        for el in arr
        if el == selected_el
    ]
    right_part = [
        el
        for el in arr
        if el > selected_el
    ]

    return quick_sort(left_part) + middle_part + quick_sort(right_part)

arr = get_arr(size_arr=5)
result = quick_sort(arr)
print(result)
    



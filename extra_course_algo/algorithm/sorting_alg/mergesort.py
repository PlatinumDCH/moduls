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


def mergesort(arr:list)->list:
    n = get_lenght(arr)
    if n <= 1:
        return arr
    
    midle_el = n // 2
    left_half = arr[:midle_el]
    right_half = arr[midle_el:]

    return merge(mergesort(left_half), mergesort(right_half))


def merge(left_part:list, right_part:list)->list:
    merged = []
    left_index = 0
    right_index = 0

    #сравнение елементов из двух частей
    while left_index < len(left_part) and right_index < len(right_part):

        if left_part[left_index] <= right_part[right_index]:
            merged.append(left_part[left_index])
            left_index += 1

        else:
            merged.append(right_part[right_index])
            right_index += 1

    #добавляем оставшейся елементы из левой части
    while left_index < len(left_part):
        merged.append(left_part[left_index])
        left_index += 1
    
    #добавляем оставшейся елементы из правой части
    while right_index < len(right_part):
        merged.append(right_part[right_index])
        right_index += 1

    return merged


if __name__ == '__main__':
    arr = get_arr(7)
    print(arr)
    r = mergesort(arr)
    print(r)
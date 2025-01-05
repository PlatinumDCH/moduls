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

def insertion_sort(arr:list) -> list:
    n = get_lenght(arr)
    for i in range(1,n):
        temp = arr[i]
        j = i - 1
        while j >= 0 and temp < arr[j]:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = temp
    return arr
    
if __name__ == '__main__':
    arr = get_arr()
    print(arr)
    r = insertion_sort(arr)
    print(arr)
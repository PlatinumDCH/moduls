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

def shellsort(arr:list) -> list:
    n = get_lenght(arr)
    gap = n//2

    while gap > 0:
        for i in range(gap,n):
            temp = arr[i]
            j = i
            while j >= gap and temp < arr[j - gap]:
                arr[j] = arr[j - gap]
                j = j - gap
            arr[j] = temp
        gap = gap//2
        return arr
    
if __name__ == '__main__':
    arr = get_arr()
    print(arr)
    r = shellsort(arr)
    print(arr)
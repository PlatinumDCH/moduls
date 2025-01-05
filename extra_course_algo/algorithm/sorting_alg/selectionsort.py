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

def selection_sort(arr:list)->list:
    n = get_lenght(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

if __name__ == '__main__':
    arr = get_arr(size_arr=5)
    r = selection_sort(arr)
    print(arr)


"""
get arr [5, 6, 3, 10, 1]
get lenght 5
range i 0->5
    i now == 0
    min index = i = 0
    [5, 6, 3, 10, 1]
    |
    min index 0
    range j (i+1, n) 1-5
    frame1 j=1
        arr[j]<arr[minindex]? 6<5 false
    frame2 j=2
        arr[j]<arr[minindex]? 3<6 true
        minindex=2  (number 3
        )
        [5, 6, 3, 10, 1]
               \
               min index
    frame3 j=3
        arr[j]<arr[minindex]? 10<3 false
    frame4 j=4
        arr[j]<arr[minindex]? 1<3 true
        [5, 6, 3, 10, 1]
                       \
                        min index
    arr[i], arr[min_index] = arr[min_index], arr[i]
      \           \                  |
     number 5    number 1      
    proces swap [1, 6, 3, 10, 5]

    repeat loops 
    ...
    result = sorting list
    
""" 
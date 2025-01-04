#0(1) константный час
def get_fist_element(arr):
    return arr[0]

#O(n) ленейное время
def find_element(arr, target):
    for item in arr:
        if item == target:
            return True
    return False

#O(n2)
def buble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                
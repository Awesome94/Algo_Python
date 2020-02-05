def quick_sort(arr):
    mid = len(arr)//2
    n = len(arr)
    pivot = arr[mid]
    temp = arr[n]
    arr[n]= pivot
    arr[mid] = temp
    for x in arr:
        pass
    return quick_sort(arr)
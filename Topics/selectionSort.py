def selectionSort(arr):
    for x in range(len(arr)-1):
        small = arr[x]
        indx = x
        for j in range(x+1, len(arr)):
            if small > arr[j]:
                small = arr[j]
                indx = j
        arr[x], arr[indx] = arr[indx], arr[x]
    return arr


print(selectionSort([10, 3, 2, 1, 54, 12, 0]))


def selectionSortV2(arr):
    for x in range(len(arr)-1):
        small_index = x
        for j in range(x+1, len(arr)):
            if arr[small_index] > arr[j]:
                small_index = j
        arr[x], arr[small_index] = arr[small_index], arr[x]
    return arr

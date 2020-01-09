def BinarySearch(arr, tar):
    L = len(arr)-1
    i = 0
    while i <= L:
        mid = i + (L - i)//2
        if arr[mid] == tar:
            return mid
        elif arr[mid] < tar:
            i = mid + 1
        else:
            L -= 1
    return -1
print(BinarySearch([1,2,3,8,9,11,15], 11))
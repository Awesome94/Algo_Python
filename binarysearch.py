def BinarySearch(arr, tar):
    """
    The binary search algorithm runs in o(logn) time
    it is used to find a specific element in a sorted array.
    Gets the midpoint of a given array and hence compare the target item with the item at mid index
    if the item is < than the mid. We then find the next mid from the current positon  and vice versa
    """
    L = len(arr)-1
    i = 0
    while i <= L:
        mid = i + (L - i)//2 # better way to calculate mid point to avoid overflow
        if arr[mid] == tar:
            return mid
        elif arr[mid] < tar:
            i = mid + 1
        else:
            L -= 1
    return -1
print(BinarySearch([1,2,3,8,9,11,15], 11))
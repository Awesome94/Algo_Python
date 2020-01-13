def findDuplicates(arr):
    mid  = len(arr)//2
    return[x for x in arr[:mid] if x in arr[mid:]]

def findDuplicates2(arr):
    for x in set(arr):
        if arr.count(x) <= 1:
            arr.pop(arr.index(x))
    return list(set(arr))
    
arr = [4,3,2,7,8,9,8,3,2,1]
print(findDuplicates(arr))
print(findDuplicates2(arr))
def subarraySort(array):
    target = sorted(array)
    n = len(array)
    result = []
    if array == target:
        return [-1, -1]
    for x in range(n):
        if array[x] != target[x]:
            result.append(x)
    return[result[0], result[-1]]

arr = [1,2,4,7,10,11,7,12,6,7,16,18,19]
arr = [2, 1]

print(subarraySort(arr))
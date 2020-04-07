def countElements(arr: [int]) -> int:
    n = len(arr)
    arr_map = {}
    for x in arr:
        if x in arr_map.keys():
            arr_map[x]=arr_map[x]+1
        else:
            arr_map[x] = 1
    result = []
    for j in range(n):
        if arr[j]+1 in arr and arr[j] not in result:
            result.append(arr[j])
    final = 0
    for i in result:
        final+=arr_map[i]
    return final

countElements([1,2,3])
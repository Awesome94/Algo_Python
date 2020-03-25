def rotate(arr):
    n = len(arr)
    n1 = len(arr[0])
    arr_map = {}
    for c in range(n1):
        for r in range(n-1, -1, -1):
            if c not in arr_map.keys():
                arr_map[c] = [arr[r][c]]
            else:
                arr_map[c].append(arr[r][c])
                
    for k, v in arr_map.items():
        if k <= len(arr)-1:
            arr[k] = v
        else:
            arr.append(v) 
    
    return arr

arr=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]
print(rotate(arr))
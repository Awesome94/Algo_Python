def hourglassSum(arr):
    results = []
    j=0
    for x in arr:
        j+=1
        for i in range(len(x)):
            if i <= len(x)-3 and j <= len(arr)-2:
                results.append(sum(x[i:i+3], arr[j][i+1]) +sum(arr[j+1][i:i+3]))
    print(len(results))
    return max(results)

arr = [
[-1, 1, -1, 0, 0, 0],
[0, -1, 0, 0, 0, 0],
[-1, -1, -1, 0, 0, 0],
[0, -9, 2, -4, -4, 0],
[-7, 0, 0, -2, 0, 0],
[0, 0, -1, -2, -4, 0]
]
print(hourglassSum(arr))
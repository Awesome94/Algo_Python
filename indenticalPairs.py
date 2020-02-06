# O(n2) Runtime || O(n) Space
def GetIndenticalPairs(arr):
    results = []
    limit = 1000000000
    counter = 0
    for x in range(len(arr)):
        j = 0
        if arr.count(arr[x]) <= 1:
            continue
        while j < len(arr):
            if arr[x] == arr[j] and x < j:
                pair = [x, j]
                counter+=1
                results.append(pair)
            if counter >=  limit: return limit
            j+=1
    print(results)
    return len(results)


arr = [3,5,6,3,3,5]
print(GetIndenticalPairs(arr))

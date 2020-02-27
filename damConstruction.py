def constructDam(pos, dams):
    arr = [-1]*(max(pos)+1)
    i = 0
    x = 1
    mud_segs = []
    while i < len(dams):
        arr[pos[i]] = dams[i]
        i += 1

    while x < len(arr):
        if x not in pos and x+1 not in pos:
            res = arr[x-1]+1
            arr[x] = res
            mud_segs.append(res)

        if x not in pos and x+1 in pos:
            res = arr[x-1]+1
            if res <= arr[x+1]:
                mud_segs.append(res)
                arr[x] = res
            else:
                res = arr[x+1]+1
                mud_segs.append(res)
                arr[x] = res
        x += 1
    return 0 if not len(mud_segs) else max(mud_segs)


print(constructDam([1, 2, 4, 7], [4, 6, 8, 11]))

# TestCases:
# Positions| Walls
# [1, 3, 7], [4, 3, 3]
# [1, 2, 4, 7], [4, 6, 8, 11]

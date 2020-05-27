def Oneup_Onedown(arr):
    arr.sort()
    x = 0
    direction = True
    n = len(arr)-1
    while x < n:
        j = x+1
        if direction and arr[x] < arr[j]:
            direction = False
            x += 1
            continue
        elif direction and arr[x] >= arr[j]:
            arr[x] -= 1
            direction = True

        if not direction and arr[x] > arr[j]:
            x += 1
            direction = True
            continue
        elif not direction and arr[x] <= arr[j]:
            arr[j] -= 1
            direction = False
    return arr


arr = [5, 4, 5, 6, 7]
arr = [5, 4, 4, 4, 3, 6]
c = [5, 6, 4, 4, 3, 4]
arr2 = [3, 3, 3, 3, 3]

print(adNums(arr))

def lengthOfLIS(num) -> int:
    num_map = {}
    n = len(num)
    max_num = 0
    nums_ranges = [0]* n
    if n <= 1: return n
    for i in range(n):
        if i == 0:
            nums_ranges[i] = 1
            continue
        prev = nums_ranges[i-1]
        if num[i] > num[i-1] and num[i] > max_num:
            max_num = num[i]
            if num[i] not in num_map.keys():
                nums_ranges[i] = prev + 1
                num_map[num[i]] = nums_ranges[i]
            else:
                nums_ranges[i] = max(prev, num_map[num[i]])
        elif num[i] > num[i-1] and num[i] < max_num:
            max_num = num[i]
            nums_ranges[i] = prev
            num_map[num[i]] = nums_ranges[i]

        else:
            if num[i] not in num_map.keys():
                nums_ranges[i] = prev
                num_map[num[i]] = nums_ranges[i]
            else:
                nums_ranges[i] = max(prev, num_map[num[i]])
    return max(nums_ranges)

arr = [
    [4,10,4,3,8,7,9],
    [10,9,2,5,3,7,101,18], 
    [],
    [0],
    [1,2], 
    [1,0], 
    [10,9,2,5,3,4], 
    [10,9,2,5,3,7,101,18],
    [3,5,6,2,5,4,19,5,6,7,12],
    [-2, -1]]
# arr = [[3,5,6,2,5,4,19,5,6,7,12]]
for k in arr:
    print(lengthOfLIS(k))

def lengthOfLIS(nums):
    lis_map={}
    n = len(nums)
    if n <= 1:
        return n

    for x in range(n-1):
        checkNext = False
        i = x+1
        temp = []
        new = []

        if x not in lis_map.keys():
            lis_map[x] = [nums[x]]

        while i < n:
            if not temp:
                prev_temp = float("-inf")
            else:
                prev_temp = temp[-1]
            if nums[i] > lis_map[x][-1] and not checkNext and nums[i] > prev_temp:
                temp.append(nums[i])
                i+=1
            else:
                checkNext = True
            
            if checkNext:
                if not new:
                    prev = 0
                else:
                    prev = new[-1]
                if nums[i] > nums[x] and nums[i] > prev:
                    new.append(nums[i])
                i+=1

        if len(new) > len(temp):
            print("this is temp1", temp)
            lis_map[x] = lis_map[x] + new
        else:
            print("this is temp", temp)
            lis_map[x] = lis_map[x] + temp
        lis_map[x] = len(lis_map[x])

    return max(lis_map.values())

print(lengthOfLIS([-2, -1]))
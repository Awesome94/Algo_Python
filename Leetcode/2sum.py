def twoSum(nums, target):
    x = 0
    results = []
    for i in range(len(nums)-1):
        print(i)
        x = i+1
        while x < len(nums):
            print(nums[i], nums[x])
            if nums[i] + nums[x] == target:
                results.append(i)
                results.append(x)
            x += 1
    return results

# print(twoSum([3, 2, 4], 6))


def fourSum(nums, target):
    nums.sort()
    quads = []
    n = len(nums)-1
    for x in range(n-2):
        for i in range(x+1, n-1):
            j = i+1
            e = n
            while j < e:
                if nums[x] + nums[i] +nums[j] + nums[e] == target:
                    quads.append([nums[x],nums[i],nums[j],nums[e]])
                    j+=1
                    e-=1
                elif nums[x] + nums[i] +nums[j] + nums[e] > target:
                    e-=1
                else:
                    j+=1
    return quads

nums = [7,6,4,-1,1,6,2]
print(fourSum(nums, 16))
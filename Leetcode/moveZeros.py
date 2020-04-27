def moveZeroes(nums):
    n = len(nums)
    x = count = 0
    while x < n:
        if nums[x] == 0:
            nums.pop(x)
            count+=1
            n = len(nums)
            continue
        n = len(nums)
        x+=1
    for j in range(count):nums.append(0)
    print(nums)

numbers = [0,0,3,0,78,0,0]
print(moveZeroes(numbers))
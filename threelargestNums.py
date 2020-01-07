def findThreeLargestNumbers(nums):
	n = len(nums)
	L_range = len(nums)-3
	for x in range(n):
		j = x+1
		while j < n:
			if nums[x]<=nums[j]:
				j+=1
			else:
				nums[x], nums[j] = nums[j], nums[x]
				j+=1
	return nums[L_range:]

nums = [141, 1, 17, -1, 17, -27, 18,541,8,7,7]
print(findThreeLargestNumbers(nums))
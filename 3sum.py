def threeSum(nums):
	"""
	:type nums: List[int]
	:rtype: List[List[int]]
	"""
	nums.sort()
	result = []
	for i in range(len(nums)-2):
		if i> 0 and nums[i] == nums[i-1]:
			continue
		l = i+1
		r = len(nums)-1
		while(l<r):
			sum = nums[i] + nums[l] + nums[r]
			if sum<30:
				l+=1
			elif sum >30:
				r-=1
			else:
				result.append([nums[i],nums[l],nums[r]])
			while l<len(nums)-1 and nums[l] == nums[l + 1] : l += 1
			while r>0 and nums[r] == nums[r - 1]: r -= 1
			l+=1
			r-=1
		return result

print(threeSum([0,3,5,7,9,11,15,15]))
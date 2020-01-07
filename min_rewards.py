def minRewards(array):
	rewardsMap = {}
	total = []
	for x in array:
		rewardsMap[x] = 1
	j = 1
	while j < len(array)-2:
		R = j+1
		L = j-1 
		if array[j] > array[L]:
			rewardsMap[array[j]] = rewardsMap[array[L]] + 1
		else:
			rewardsMap[array[L]] = rewardsMap[array[j]] + 1
		if array[j] > array[R]:
			rewardsMap[array[j]] = rewardsMap[array[R]] + 1
			if array[L] > array[j] and rewardsMap[array[L]]<=rewardsMap[array[j]]:
				j-=1
				continue
		else:
			rewardsMap[array[R]] = rewardsMap[array[j]]+ 1
		
		j+=1
	print(rewardsMap)
	for _, v in rewardsMap.items():
		total.append(v)

	return sum(total)

arr = [0,4,2,1,3]
# arr = [8,4,2,1,3,6,7,9,5]
print(minRewards(arr))

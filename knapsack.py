def getKnapsackItems(knapscakValues, items):
	sequence=[]
	i = len(knapscakValues)-1
	print(items)
	c = len(knapscakValues[0])-1
	while i > 0:
		# print(i, knapscakValues[i][c], knapscakValues[i-1][c])		
		if knapscakValues[i][c]  == knapscakValues[i-1][c]:
			i-=1
		else:
			# print("i-1", i)
			sequence.append(i-1)
			c-= items[i-1][1]
			i-=1
		if c == 0:
			break
	return list(reversed(sequence))

def knapsackProblem(capacity, items):
	knapsackValues  = [[0 for x in range(0, capacity+1)] for y in range(0, len(items)+1)]
	for i in range(1, len(items)+1):
		currentWeight  = items[i-1][1]
		currentValue = items[i-1][0]
		
		for c in range(0, capacity+	1):
			if currentWeight>c:
				knapsackValues[i][c] = knapsackValues[i-1][c]
			else:
				knapsackValues[i][c] = max(knapsackValues[i-1][c], knapsackValues[i-1][c-currentWeight] + currentValue)
	return [knapsackValues[-1][-1], getKnapsackItems(knapsackValues, items)]
		
		
arr = [[1, 2],[4,3],[5, 6],[6,7]]
print(knapsackProblem(10, arr))

def ficn('word'):
	while k < len(word):
		if word[k] in 
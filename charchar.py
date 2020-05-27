class Solution:
	def __init__(self, size):
		self.size = size
		self.ans = [-1]*(size+1)
		self.n = size

	def solve(self, n=0, counter=0):
		for i in range(1, self.size+1):
			if self.n <= 0:
				self.ans[n] = n
			if  self.n < 5 and self.n:
				counter+=1
				self.ans[n] = n

		# if self.ans[self.size] != -1:
		# 	new = self.ans[self.size] + counter
		# 	print("nw", new)
		# 	return new

		if self.n < 5:
			self.ans[self.size] = self.n
			return self.n
		if self.n == 5:
			self.ans[self.size] = 1
			counter+=1
			return 1
		elif 10 > self.n > 5:
			self.n = self.n-5
			counter+=1
		elif 10 <= self.n < 25:
			self.n = self.n-10
			counter+=1
		else:
			self.n = self.n-25
			counter += 1
		result = self.solve(self.n, counter)
		self.ans[self.size] = result
		print(result)
		print(self.ans)


x = Solution(7).solve()
print(x)
# print(x.solve(56991))

class Solution:
    def __init__(self, size):
        self.size = size
        self.sub_sols = [-1]*(size+1)
    
        for n in range(1, size+1):
            if n < 5:
                self.sub_sols[n] = n
            elif n == 5 or n==10 or n == 25:
                self.sub_sols[n] = 1
            elif 10 > n > 5:
                self.sub_sols[n] = self.sub_sols[n-5] + self.sub_sols[5]
            elif 25 > n >10:
                self.sub_sols[n] = self.sub_sols[n-10] + self.sub_sols[10]
            elif n > 25:
                self.sub_sols[n] = self.sub_sols[n-25] + self.sub_sols[25]
            else:
                self.sub_sols[n] = self.sub_sols[-3]
        print(self.sub_sols[n])
x = Solution(56991)
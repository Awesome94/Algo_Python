class Solution:
    def __init__(self, arr, size):
        self.arr = arr
        self.size = size
        self.sub_sols = [-1]*max(max(self.arr)+1, (size+1))
    
    def find_max_div(self, n):
        max_div = 0
        for x in self.arr:
            if n%x == 0:
                max_div = x
        return max_div
    
    def find_denoms(self):
        for i in self.arr:
            self.sub_sols[0] = 0
            self.sub_sols[i] = 1

        if self.sub_sols[self.size] != -1:
            print(self.sub_sols[self.size])
            return self.sub_sols[self.size]

        for x in range(1, self.size+1):
            max_div = self.find_max_div(x)
            first_val = self.sub_sols[x-max_div]+self.sub_sols[max_div]
            second_val = self.sub_sols[x-1]+self.sub_sols[x-(x-1)]
            self.sub_sols[x] = min(first_val, second_val)
        print(self.sub_sols[x])
        return self.sub_sols[x]
    
       
# x = Solution(56991)
x = Solution([1,5,25,10], 56991).find_denoms()



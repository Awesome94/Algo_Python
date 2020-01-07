s= ['H', 'E', 'L', 'L', 'o']
c="Hello"
class Solution(object):
    def reverseString(self, s):
        if not len(s):
            return s
        else:
            return [s[-1]] + self.reverseString(s[:-1])
    
soln = Solution()
print(soln.reverseString(s))

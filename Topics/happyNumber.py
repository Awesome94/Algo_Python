# def isHappy(n: int) -> bool:
#     str_int = str(n)
#     ans = 0
#     int_len = len(str_int)
#     for x in str_int:
#         ans+=int(x)**2
#         if ans//(10**int_len)==1:
#             print("true", int_len) 
#             return True
#     isHappy(ans)


class Solution:
    def __init__(self):
        self.pow_arr = [x**2 for x in range(10)]
    def isHappy(self, n: int) -> bool:
        if n==1:return True
        print(n)
        str_int = str(n)
        ans = 0
        int_len = len(str_int)
        try: 
            for x in range(int_len):
                ans+=self.pow_arr[int(str_int[x])]
            if ans > 162:
                return False
            return self.isHappy(ans)
        except:
            return False
        
happy = Solution()
print(happy.isHappy(112))
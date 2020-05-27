def arrProd(nums):
    n = len(nums)
    final = []
    for i in range(n):
        result = 1
        for j in range(n):
            if j == i:
                continue
            result*=nums[j]
        final.append(result)
    return final

def arrProdTwo(nums):
    prod = 1
    n = len(nums)
    for x in nums:
        prod*=x
    for i in range(n):
        nums[i] = prod//nums[i]
    return nums
def arrProdTwo(nums):
    n = len(nums)
    temp = nums
    result = []
    while x < n:
        temp.remove(x)
        

print(arrProdTwo([1,2,3,4]))
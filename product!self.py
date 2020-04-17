def produsctExceptSelf1(nums):
    n = len(nums)
    i = 0
    result = []
    prod =1
    j = 1
    while i < n:
        if j == n:
            result.append(prod)
            prod=1
            i+=1
            j = i+1
        else:
            prod*=nums[j]
            j+=1
    prod = 1
    for x in range(1, n):
        prod*=nums[x-1]
        result[x]*=prod

    return result
def productExceptSelf(nums):
    n = len(nums)
    result = [0]*n
    result[n-1]=1
    prod = 1
    for j in range(n-1, -1, -1):
        if result[j] == 1:
            continue 
        result[j] = nums[j+1]*result[j+1]
    
    for x in range(1, n):
        prod*=nums[x-1]
        result[x]*=prod
    return result
print(productExceptSelf([1,2,3,4]))
    






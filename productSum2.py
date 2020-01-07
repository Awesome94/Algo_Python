def productSum(array, multiplier=1):
    sum = 0
    for element in array:
        if type(element) is not list:
            sum+=element
        else:
            sum+=productSum(element, multiplier+1)
    return sum*multiplier

nums=[1,2,3,4,5]
print(productSum(nums))
def find_sum(x, multiplier, results):
    if isinstance(x, int):
        if multiplier in results:
            results[multiplier].append(x)
        else:
            results[multiplier] = [x]
    else:
        if multiplier not in results:
            results[multiplier] = []
        multiplier+=1
        for i in x:
            find_sum(i, multiplier, results)

    return results

def productSum(array):
    multiplier = 1
    currentSum = 0
    max_key = 0
    results = {}

    for x in array:
        final=find_sum(x,multiplier, results)
    for _, v in final.items():
        final[_] = sum(v)
        if max_key < _:
            max_key=_
    if max_key > 1:
        while max_key>1:
            currentSum = final[max_key]*max_key + final[max_key-1]
            final[max_key-1] = currentSum
            max_key-=1
    else:
        currentSum = final[max_key]
    return currentSum


# nums = [5,2,[7,-1],3,[6,[-13,8],4]]
# 5+2+2(7,-1)+3
nums = [1,2,3,4,5]
# nums =[[1, 2], 3, [4, 5]]
# nums = [[[[[5]]]]]
print(productSum(nums))

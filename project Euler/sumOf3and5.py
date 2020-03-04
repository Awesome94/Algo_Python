def findSum(n):
    result = []
    for x in range(n):
        if x%3==0 or x%5==0:
            result.append(x)
    return sum(result)

print(findSum(1000))
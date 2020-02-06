def getSmallestNum(n):
    power = len(str(n))
    base = pow(10, power-1)
    if n < 10:
        return 0
    if base <= n:
        return base


print(getSmallestNum(1250))
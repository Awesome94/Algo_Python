def isPrime(n):
    for x in range(2, n):
        if n%x == 0:
            return False
    return n > 1

def largestPrime(num, div=1):
    end_num = num//div
    start_num = end_num//2
    while start_num > 0 and start_num < end_num:
        x = range(start_num, end_num)
        for i in x:
            print("checking i and x = ", i, x, num%i==0)
            if isPrime(i) and num%i==0:
                return i
        end_num=start_num
        start_num=start_num//2
    return None
print(largestPrime(6008514751430, 10000000))
# 13195

import math
def getFactors(number):
    factors = []
    for n in range(1,int(math.sqrt(number))):
        if number % n == 0:
            factors.append(n)
            factors.append(number // n)
    return factors

def isPrime(number):
    return len(getFactors(number)) == 2 

def largestFactor(number):
    allfactors = getFactors(number)
    largestFactor = 0
    for factor in allfactors:
        if isPrime(factor) and factor > largestFactor:
            largestFactor = factor
    return largestFactor
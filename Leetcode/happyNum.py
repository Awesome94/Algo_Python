def isHappy(num, results=[]):
    num3 = 0
    if num == 1:
        return True

    for num2 in str(num):
        num3 += int(num2)**2

    if num3 not in results:
        results.append(num3)
    else:
        return False
    return isHappy(num3, results)

print(isHappy(1001))
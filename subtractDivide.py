# o(n) runtime n being the number given
# O(1) Space
def subtractDivide(n):
    steps = 0
    while n > 0:
        if n%2 == 0:
            n = n/2
        else:
            n = n-1
        steps+=1
    return steps

print(subtractDivide(29))

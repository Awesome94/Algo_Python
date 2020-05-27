def solutions(S):
    # write your code in Python 3.6
    n = int(S)
    steps = 0
    while  n > 0:
        if n%2 == 0:
            n = n/2
        else:
            n = n-1
        steps+=1
    return steps

print(solution('011100'))

def solution(S):
    # write your code in Python 3.6
    n = int(S, 2)
    steps = 0
 
    while  n > 0:
        if n%2 == 0:
            n = n//2
        else:
            n = n-1
        steps+=1
    return steps
# O(n) Runtime || O(n) Space
def solution(A):
    out = {}
    counter = 0
    for x in A:
        if x in out:
            counter+=out[x]
            out[x]+=1
        else:
            out[x] = 1
    return counter

A = [3,5,6,3,3,5]
print(solution(A))

{3: 1}
1

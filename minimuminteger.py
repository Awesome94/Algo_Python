def solution(arr):
    a = set(arr)
    m = max(a)
    if m < 0:
        return 1
    else:
        for x in range(1, m):
            if x not in a:
                return x
        return m+1
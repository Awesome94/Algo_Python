def solution(N):
    bin_n = bin(N)
    binary = bin_n[2:]
    results = {}
    counts = binary.count('1')
    gap = 0
    for x in binary:
        while counts > 0:
            if x == '1':
                results[counts] = gap
                counts -= 1
                gap=0
            else:
                gap+=1
            break
    return max(list(results.values()))

print(solution(1041))

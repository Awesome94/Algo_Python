def insertMintoN(N, M, i=0, j=0):
    allOnes = -1
    left = allOnes << (j+1)
    right  = ((1<<i)-1)
    mask = left | right
    n_cleared = N & mask
    m_shifted = M << i
    return n_cleared | m_shifted
# print(insertMintoN(1024, 19, 2, 6))

def binTostring(num):
    result = "0."
    if num > 1 or num < 0:
        return "Error"
    while num!=0:
        if len(result) > 32:
            return "Error"
        num*=2
        if num >= 1:
            result+="1"
            num-=1
        else:
            result+="0"
    return result
print(binTostring(1.625))
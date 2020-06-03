def stringComp(s):
    n = len(s)
    i, count = 0, 1
    result = ""
    prev = s[0]
    for i in range(1, n):
        if s[i] == prev:
            count+=1
        else:
            result += f"{prev}{count}"
            count = 1
            prev = s[i]
    result += f"{prev}{count}"
    if len(result) < n:
        return result
    else:
        return s
    
print(stringComp("aabcccccaaa"))
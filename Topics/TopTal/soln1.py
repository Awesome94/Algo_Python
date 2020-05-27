def countStr(S, k):
    n = len(S)
    r = k
    i = 0
    current_length = len(CompressStr(S))
    while i < n:
        new_s = S[:i] + S[i+r:]
        new_length = len(CompressStr(new_s))
        if new_length < current_length:
            current_length = new_length
        i+=1
    return current_length

def CompressStr(stringElem):
    counter = 1
    n = len(stringElem)
    current_Str = stringElem[0]
    result = ""
    for k in range(1, n):
        if stringElem[k] == current_Str:
            counter+=1
        else:
            if counter <= 1:
                counter = ""
            result+=str(counter)
            result+=current_Str
            counter = 1
            current_Str = stringElem[k]
    result+=str(counter)
    result+=current_Str
    return result


print(countStr("AAAAAAAAAAABXXAAAAAAAAAA", 3))



component 
ontouch 

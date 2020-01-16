def toUpperCase(string):
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    str_lst = [s for s in string]
    for x in string:
        if x in lower:
            str_lst[str_lst.index(x)] = upper[lower.index(x)]
    return "".join(str_lst)
# o(n) runtime and o(n) space

def toLowerCase(string):
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    str_lst = [ x for x in string]
    for s in string:
        if s in upper:
            str_lst[str_lst.index(s)] = lower[upper.index(s)]
    return "".join(str_lst)
# o(n) runtime and o(n) space   

print(toUpperCase("This is it"))
print(toLowerCase("THIS IS IT"))
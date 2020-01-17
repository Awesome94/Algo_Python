# given a list of strings return a list of xters that appear in all strings
def common_characters(lst):
    i = 0
    lst1 = lst[0]
    n = len(lst1)
    final = {}
    while i < n:
        for x in range(1, len(lst)):
            if lst1[i] in lst[x]:
                idx = lst[x].index(lst1[i])
                commonChar = lst1[i]
                lst[x] = lst[x][:idx] + lst[x][(idx+1):]
            else:
                commonChar = ""
      
            final[i] = commonChar
        i+=1
    return[x for x in final.values() if x]
print(common_characters(['google', 'facebook', 'youtube']))

# o(n)space o(n)time complexity
def lonely_num(arr):
    result = {}
    for x in arr:
        if x not in result.keys():
            result[x] = 0
        result[x] +=1

    for _, v in result.items():
        if v <= 1:
            return _



print(lonely_num([4, 4,6, 1, 3, 1, 3]))
        
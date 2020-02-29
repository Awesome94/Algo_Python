def myAtoi(var_str: str) -> int:
    results = {
        'digit_indx': 0,
        'var_str_indx': len(var_str)
    }
    opsCount = 0
    ops = ['+', '-']
    var_str_int = ""
    bannedChars = ['~', '!', '@', '$', '%', '^', ',', '&', '*', '',
                   '(', ')', ',', '_', '}', '{', '"', '|', '?', '>', '<', '.']
    allDigits = False

    for x in var_str:
        if x.isdigit() or x in ops:
            results["digit_indx"] = var_str.index(x)
            break
    for s in var_str:
        if s.isalpha() or s in bannedChars:
            results["var_str_indx"] = var_str.index(s)
            break

    if results["var_str_indx"] < results["digit_indx"]:
        return 0

    for i in range(results["digit_indx"], results["var_str_indx"]):
        if var_str[i] in ops and not len(var_str_int):
            var_str_int += var_str[i]
        elif var_str[i].isdigit():
            var_str_int += var_str[i]
        else:
            break
    for n in var_str_int:
        if n.isdigit() and opsCount <= 1:
            allDigits = True
        else:
            opsCount += 1
    if not allDigits:
        return 0
    if int(var_str_int) < pow(-2, 31):
        return pow(-2, 31)

    return int(var_str_int)


print(myAtoi("    -47"))

def print_r(n=0):
    print(n)
    if n ==10:
        return
    return print_r(n+1)


print(print_r())
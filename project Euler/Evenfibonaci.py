def addEvenFiboonacci(n):
    x=1
    y=2
    arr = []
    while y <= n:
        if x%2 == 0 and x not in arr:
            arr.append(x)
        if y%2 == 0 and y not in arr:
            arr.append(y)
        next = y+x
        x = next
        y = x + y
        if x%2 == 0:
            arr.append(x)
        if y%2 == 0:
            arr.append(y)
    return sum(arr)

print(addEvenFiboonacci(4000000))
[1, 2, 3, 5]
        
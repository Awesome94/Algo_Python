def smallestMultiple(n):
    multiples = [1]*(n+1)
    x  = 3
    i=1
    while x <= n:
        if x <= 2:
            multiples[x] = x
        previous = multiples[x-1]
        while i <= x:
            if previous%i != 0:
                previous=previous+multiples[x-2]
                i=1
            else:
                i+=1
        multiples[x] = previous
        x+=1
    return multiples[-1]

print(smallestMultiple(20))

    

def findNthPrimeNo(n, num):
    limit = 0
    prime = True
    prime_lst = []
    while limit <= n:
        for x in range(2, num):
            if len(prime_lst) == n:
                return prime_lst[n-1]
            for y in range(2, x):
                if x % y==0:
                    break
            else:
                limit+=1
                if x not in prime_lst:
                    prime_lst.append(x)
    return x, limit, prime_lst


print(findNthPrimeNo(10001, 100000))
def waterCan(used, total):
    n = len(used)
    count = 0
    for i in range(n):
        j = 0
        while j < n:
            if j == i:
                j+=1
                continue
            sum_used = used[i] + used[j]
            if  sum_used <= total[i]:
                used[i] = sum_used
                used[j] = 0
            j+=1
    for x in used:
        if x > 0:
            count+=1
    return count
   

# used = [1,1,1]
# total = [3,3,3]



used = [3,2,1,3,1]
total = [3,5,3,5,5]
# total = [3,3,3]
# used = [2, 2, 3]
# total = [3,3,3]
# used = [1, 2, 3]
print(waterCan(used, total))
















nums = [7,6,4,-1,1,2]
target = 16
sort nums
[-1,1,2,4,6,7]


-1,1,2 7= 9 => move idx[2]+1
-1,1,4,7 = 11  => still less than the target so we move idx[2]+1
-1,1,-6,7 => 15 still less 

-1,2,4,7 = 12 => lees than target
-1, 2, 6, 7 = 15 => still less

-1, 4, 6, 7 = 16=> save this one.

1,2,4,7 => 14 which is less than target
1,2,6,7 => 16 = > append to array

1,4,6,7 = 18 = > greater than target. so we move last index to n-1 only if it greater than index "j"
No more possible moves so we move to the next one


2,4,6,7 = > 19 => no more moves

currentIndex = x
following index  = i
third index  = j
 finalIndex = n

quad = []
n = len(array)-1
for x in range(n-2):
    for i in range(x, n-1):
        if array[i] == array[j]:
            continue
        while j < n:
            if array[x] + array[i] +array[j] + array[n] == target:
                quads.append(array[x],array[i],array[j],array[n])
            elif array[x] + array[i] +array[j] + array[n] > target:
                n-=1
            else:
                j+=1
    return quad







[-1,1,2,4,6,6,7]
-1,2,4,7 = 12
-1,2,6,7 = 16=>append
-1,2,6,7

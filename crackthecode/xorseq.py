import math
def maxSubsequenceLength(n, arr, k):
    sequences = [None]*n
    length = [1]*n
    max_ind = 0
    result = []

    for i in range(n):
        for j in range(i):
            if arr[i]^arr[j] == k:
                length[i] =  length[j]+length[i]
                sequences[i] = j
        if length[i] > length[max_ind]:
            max_ind = i
    while max_ind:
        result.append(arr[max_ind])
        max_ind = sequences[max_ind]

    return result[::-1]
# arr = [2,1,3,5,2]
arr = [1, 2, 3, 4, 5]
n = len(arr)
k=4
# print(maxSubsequenceLength(n, arr, k))

def subsetXOR(arr, n, k): 
    max_ele = arr[0] 
    for i in range(1, n): 
        if arr[i] > max_ele : 
            max_ele = arr[i] 
    m = (1 << (int)(math.log2(max_ele) + 1)) - 1
    print("this is m", m)
    sequences = [[0 for i in range(m + 1)] 
             for i in range(n + 1)] 
      
    sequences[0][0] = 1
  
    for i in range(1, n + 1): 
        for j in range(m + 1): 
            sequences[i][j] = (sequences[i - 1][j] + sequences[i - 1][j ^ arr[i - 1]]) 
    return sequences[n][k] 

print(subsetXOR(arr, n, k))
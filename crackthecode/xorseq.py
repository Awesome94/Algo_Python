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
arr = [2,1,3,5,2]
n = len(arr)
k=2
print(maxSubsequenceLength(n, arr, k))
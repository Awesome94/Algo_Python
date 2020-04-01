def longestIncreasingSubsequence(arr):
    n = len(arr)
    lengths = [1]*n
    sequences = [None]*n
    max_index = 0
    sequence = []
    
    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i] and lengths[j] + 1 >= lengths[i]:
                lengths[i] = lengths[j]+1
                sequences[i] = j 
        if lengths[i] > lengths[max_index]:
            max_index = i

    while max_index is not None:
        sequence.append(arr[max_index])
        max_index = sequences[max_index]

    return list(reversed(sequence)) 

print(longestIncreasingSubsequence([5,7,-24,12,13,2,3,12,5,6,35]))

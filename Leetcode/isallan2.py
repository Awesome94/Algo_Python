
def longestIncreasingSubsequence(arr):
    subseq = []
    subseq_len = {}
    secondLastElement = None
    n = len(arr)
    if n < 1: return 0 
    for i in range(n):
        subseq.append([arr[i]])
        current_subseq = subseq[i]

        if subseq_len and arr[i] >= max(subseq_len.keys()):
            continue

        for j in range(i+1, n):
            lastElement = current_subseq[-1]

            if len(current_subseq) > 1:
                secondLastElement = current_subseq[-2]

            if arr[j] > lastElement:
                current_subseq.append(arr[j])

            if arr[j] < lastElement and secondLastElement and arr[j] > secondLastElement:
                current_subseq.pop()
                current_subseq.append(arr[j])
        subseq_len[arr[i]] = current_subseq

    max_len = list((subseq_len.values()))
    
    c = [max(len(x) for x in max_len)]

    for _, v in subseq_len.items():
        if len(v) == c[0]:
            return v
    
print(longestIncreasingSubsequence([5,7,-24,12,13,2,3,12,5,6,35]))
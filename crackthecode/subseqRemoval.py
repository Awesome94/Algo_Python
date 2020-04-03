def subsequenceRemoval(arr, n):
    arr_map = {}
    n = len(arr)
    for x in arr:
        if x in arr_map:
            arr_map[x]+=1
        arr_map[x]=0

    max_sub = []
    for i in range(n):
        if arr_map[arr[i]] > 0:
            subseq = [arr[i]]
        else:
            continue
        for j in range(i+1, n):
            if  arr[j] >= subseq[-1]:
                subseq.append([arr[j]])
        if len(subseq) > len(max_sub):
            max_sub = subseq
    return max_sub


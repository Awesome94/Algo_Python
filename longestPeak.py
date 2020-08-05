def longestPeak(arr):
    increasing =  False 
    decreasing = False
    count  = max_length = 0
    for i in range(len(arr)-1):
        current = arr[i]
        next_val = arr[i+1]

        if current < next_val:
            count+=1
            increasing = True
        
        if current == next_val:
            count = 0
            increasing = False
            decreasing = False
        
        if current > next_val and increasing == True:
            count += 1
            max_length = max(max_length, count)
            decreasing=True

        if current < next_val and decreasing == True:
            count = 0
            decreasing = False
        
        if i+1 == len(arr)-1 and decreasing == True:
            max_length = max(max_length, count+1)
            

    return max_length
arr = [1, 3, 2, 1]
print(longestPeak(arr))
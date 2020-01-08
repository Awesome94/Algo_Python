def minRewards(arr):
    rewards = {}
    min_rewards = []
    for x in arr:
        rewards[x] = 1
    for x in range(len(arr)-1):
        i = x+1
        j = x-1
        if arr[x] > arr[i] and rewards[arr[x]] <= rewards[arr[i]]:
            rewards[arr[x]] = rewards[arr[i]]+1
        elif arr[x] < arr[i] and rewards[arr[x]] >= rewards[arr[i]]:
            rewards[arr[i]] = rewards[arr[x]]+1

        while j >= 0:
            z = j+1
            if arr[j] > arr[z] and rewards[arr[j]] <= rewards[arr[z]]:
                rewards[arr[j]] = rewards[arr[z]]+1
            j-=1
    for _, v in rewards.items():
            min_rewards.append(v)
    return min_rewards
    
arr = [8,4,2,1,3,6,7,9,5]
print(minRewards(arr))


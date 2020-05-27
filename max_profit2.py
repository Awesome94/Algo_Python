def maxProfit(prices):
    n = len(prices)
    arr = [-1]*n
    for x in range(n):
        arr[x] = prices[x]-min(prices[:x+1])
    
    return max(arr)

arr = [7,1,5,3,6,4]
print(maxProfit(arr))
def maxProfit(prices):
    n = len(prices)
    price_grid  = [[0 for x in range(0, n)] for y in range(0, n)]
    days_map = {}
    max_profit = 0
    for i in range(n):
        for j in range(i+1, n):
            if prices[j] <= prices[i]:
                continue
            diff = prices[j]-prices[i]
            price_grid[i][j] = diff

    for col in range(n):
        print("imn the beginging", col)
        x = 0
        current_profit = 0
        days = {}
        results = [0]*n
        while col < n:
            print("this is col", col, x)
            if price_grid[x][col] > 0:
                print("this is awesome",x, col,  price_grid[x][col])
                current_profit=current_profit+price_grid[x][col]
                if col not in days.keys():
                    days[col] = {str(x):col}
                else:
                    days[col].update({str(x):col})
                x=col+1
                col+=1
                continue
            col+=1
        print(x, col, current_profit)
        if current_profit > max_profit:
            max_profit = current_profit
            days_map = days
        results[i] = max_profit
    print(price_grid)
    return max_profit

# arr = [7,1,5,3,6,4]
arr = [6,1,3,2,4,7]
# arr = [1,2,3,4,5]
# arr = [7,6,4,3,1]
print(maxProfit(arr))
[
    [0, 0, 0, 0, 0, 1],
    [0, 0, 2, 1, 3, 6], 
    [0, 0, 0, 0, 1, 4], 
    [0, 0, 0, 0, 2, 5], 
    [0, 0, 0, 0, 0, 3], 
    [0, 0, 0, 0, 0, 0]
]
[7 ]

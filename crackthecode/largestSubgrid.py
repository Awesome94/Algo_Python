def largestSubgrid(grid, maxSum):
    n = len(grid)
    for row in range(n):
        if row == 1:
            if maxSum < max([x for y in grid for x in y]):
                ans = 0
                continue
        for col in row:
            grid[row][col]
        if current_sum > maxSum:
            ans = 0
            maxSum = current_sum
        ans+=1
    return ans

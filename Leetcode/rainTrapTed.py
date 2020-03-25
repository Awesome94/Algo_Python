def trap(height:[int]) -> int:
    n = len(height)
    prev_right = 0
    prev_left = 0
    right = []
    left = []
    final = []
    # Tally to the right
    for i in range(n):
        if prev_right > height[i]:
            right.append(prev_right)
        else:
            right.append(height[i])
            prev_right = height[i]

    # Tally to the left
    for i in range(n-1, -1, -1):
        if prev_left > height[i]:
            left.append(prev_left)
        else:
            left.append(height[i])
            prev_left = height[i]
    
    left  = left[::-1]
    x=0
    while x < n:
        final.append(min(right[x], left[x])-height[x])
        x+=1
    return sum(final)

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(trap([0,2,0]))
print(trap([2,1,0,2]))
print(trap([5,4,1,2]))
print(trap([0,7,1,4,6]))
print(trap([4,9,4,5,3,2]))
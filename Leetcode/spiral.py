def spiralTraverse(arr):
    results = []
    if not arr: return results
    x0 = len(arr)
    y0 = len(arr[0])
    final_len = x0 * len(arr[0])
    y1=y=x=x1 = 0

    MoveRight = True
    MoveDown = False
    MoveLeft = False
    MoveUp = False
    
    for i in range(final_len):
        if len(results) == final_len:
            return results
        while MoveRight and y < y0:
            if len(results) == final_len:
                 return results
            results.append(arr[x][y])
            y+=1
        MoveDown = True
        x1 += 1
        x+=1
        y-=1
        MoveRight=False
        
        while MoveDown and x < x0:
            if len(results) == final_len:
                 return results
            results.append(arr[x][y])
            x+=1
        MoveLeft = True
        x0-=1
        x-=1
        y-=1
        MoveDown = False
        
        while MoveLeft and y >= y1:
            if len(results) == final_len:
                return results
            results.append(arr[x][y])
            y-=1
        MoveUp = True  
        y+=1
        y1+=1 
        y0-=1
        x-=1
        MoveLeft = False

        while MoveUp and x >= x1:
            print(x, x1)
            if len(results) == final_len:
                 return results
            results.append(arr[x][y])
            x-=1
        x = x1
        y = y1
        MoveRight = True
        MoveUp = False
    return results
# arr = [[1,2,3,4],
#         [5,6,7,8],
#         [9,10,11,12]
# ]
arr = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
arr = [[],[]]
print(spiralTraverse(arr))

[1,2,3,4,8,12,11,10,9,5,6,7]
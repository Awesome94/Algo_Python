[
   a =  [1, 3, 4, 10],
   b =  [2, 5, 9, 11],
   c =  [6, 8, 12, 15],
   d =  [7, 13, 14, 16],
]
# [a[0], b[0], a[1], a[2], b[1], c[0], d[0], c[1], b[2], a[3], b[3], c[2], d[1], d[2], c[3], d[3] ]
# 0,0,1,2,1,0,0,1,2,3,3
 def zigzag(arr):
    len_arr = len(arr)
    top = arr[0]
    x = 0
    result = []
    while x < len_arr:
        j=x+1
        if x == 0:
            result.append(arr[x][0])
            result.append( arr[j][0])
            

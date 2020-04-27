def flip_and_invert_image(matrix):
    k = len(matrix[0])
    for row in matrix:
        row.reverse() 
        for i in range(k):row[i] ^= 1
    return matrix
arr=[
  [1,1,0,0],
  [1,0,0,1],
  [0,1,1,1], 
  [1,0,1,0]
]
print(flip_and_invert_image(arr))
print(flip_and_invert_image([[1,0,1], [1,1,1], [0,1,1]]))
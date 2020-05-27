def setMatrixZeroes(matrix: [[int]])->None:
    range_lst = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                range_lst.append([i,j])

    for row_col in range_lst:
        r = row_col[0]
        c = row_col[1]
        x=y=0

        while x < len(matrix):
            matrix[x][c] = 0
            x+=1
        while y < len(matrix[0]):
            matrix[r][y] = 0
            y+=1

    return matrix

matrix= [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
print(setMatrixZeroes(matrix))

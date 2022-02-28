def removeIslands(matrix):
    # Write your code here.

    noRows = len(matrix)-1
    noCols = len(matrix[0])-1

    visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    
    for row in range(len(matrix)):
        if not visited[row][0]:
            if matrix[row][0] == 1: 
                markVisited(matrix, visited, row, 0)
            else: visited[row][0] = True
        
    for row in range(len(matrix)):
        if not visited[row][noCols]:
            if matrix[row][noCols] == 1: 
                markVisited(matrix, visited, row, noCols)
            else: visited[row][noCols] = True
                
    for col in range(len(matrix[0])):
        if not visited[noRows][col]:
            if matrix[noRows][col] == 1:
                markVisited(matrix, visited, noRows, col)
            else: visited[noRows][col]

    for col in range(len(matrix[0])):
        if not visited[0][col]:
            if matrix[0][col] == 1:
                markVisited(matrix, visited, 0, col)
            else: visited[0][col]
            
    for r in range(1, len(matrix)-1):
        for c in range(1, len(matrix[0])-1):
            if matrix[r][c] == 1 and not visited[r][c]:
                matrix[r][c] = 0
                visited[r][c] = True
            else:
                visited[r][c] = True
                
    return matrix

        
def markVisited(matrix, visited, row, col):
    if row + 1 < len(matrix) and not visited[row+1][col]:
        visited[row+1][col] = True
        if matrix[row+1][col] == 1:
            markVisited(matrix, visited, row+1, col)
    
    if row - 1 > 0 and not visited[row-1][col]:
        visited[row-1][col] = True
        if matrix[row-1][col] == 1:
            markVisited(matrix, visited,row-1,col)
            
    if col + 1 < len(matrix[0]) and not visited[row][col + 1]:
        visited[row][col + 1] = True
        if matrix[row][col + 1] == 1:
            markVisited(matrix, visited,row,col + 1)
    
    if col - 1 > 0 and not visited[row][col - 1]:
        visited[row][col - 1] = True
        if matrix[row][col - 1] == 1:
            markVisited(matrix, visited,row,col - 1)

matrix = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1]
  ]

print(removeIslands(matrix))
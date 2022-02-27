def riverSizes(matrix):
    # Write your code here.
    # 0 is land
    # 1 is (part) river
    rivers = []
    visited = [[False for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            
            if not visited[row][col]:
                if matrix[row][col] == 1:
                    riverLen = DFS(matrix, visited, row, col, 0)
                    rivers.append(riverLen)
                else:
                    visited.append((row,col))
                    
    return rivers
                    
def DFS(matrix, visited, row, col, counter):
    if matrix[row][col] != 1 or visited[row][col]:
        return
    else:
        visited[row][col] = True
        counter += 1
        
        if row + 1 < len(matrix):
             return DFS(matrix, visited, row + 1, col, counter)
             
        if row - 1 >= 0:
            return DFS(matrix, visited, row - 1, col, counter)
            
        if col+1 < len(matrix[0]):
            return DFS(matrix, visited, row, col + 1, counter)
        
        if col - 1 >= 0:
            return DFS(matrix, visited, row, col - 1, counter)
        
        return counter

matrix = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0]
  ]

print(riverSizes(matrix))
def removeIslands(matrix):
    # Write your code here.
	visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
	
	for row in range(1, len(matrix)):
		if matrix[row][0] == 1 and not visited[row][0]:
			markVisited(matrix, visited, row, 0)
				
	for col in range(1, len(matrix[0])):
		if matrix[0][col] == 1 and not visited[0][col]:
			markVisited(matrix, visited, 0, col)
			
	for r in range(1, len(matrix)-1):
		for c in range(1, len(matrix[0])-1):
			if matrix[r][c] == 1 and not visited[r][c]:
				matrix[r][c] = 0
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
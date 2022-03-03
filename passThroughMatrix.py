def passThroughMatrix(matrix):
	noSwitches = 0
	allNegative = True
	for col in range(len(matrix[0])):
		for row in range(len(matrix)):
			if matrix[row][col] < 0:
				switch = hasPositiveNeighbor(matrix, row, col)
				if switch:
					allNegative = False
					noSwitches += 1
					matrix[row][col] = matrix[row][col] * -1
					
	return noSwitches, allNegative
					
def hasPositiveNeighbor(matrix, row, col):
	nextRow = row + 1
	prevRow = row - 1
	nextCol = col + 1
	prevCol = col - 1
	
	if nextRow < len(matrix) and matrix[nextRow][col] > 0:
		return True
	
	if prevRow > 0 and matrix[prevRow][col] > 0:
		return True
	
	if nextCol < len(matrix[0]) and matrix[row][nextCol] > 0:
		return True
	
	if prevCol > 0 and matrix[row][prevCol] > 0:
		return True
	
	return False
	
	
	


def searchInSortedMatrix(matrix, target):
    # Write your code here.
	# brute force
	for row in range(len(matrix)):
		for col in range(len(matrix[0])):
			if matrix[row][col] == target:
				return [row, col]
			
	return [-1, -1]

## COMPLEXITY:
# time -> O(h * w) where h is the height and w is the width of the matrix
# space -> O(1)
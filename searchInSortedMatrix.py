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

def _searchInSortedMatrix(matrix, target):
    # Write your code here.
    
    # check last column and see if the value is bigger
         # if bigger => get the previous item
         # if smaller => go to next line
    
    for row in range(len(matrix)):
        col = len(matrix[0])-1
        
        while col >= 0:
            curVal = matrix[row][col]
            if curVal == target:
                return [row,col]
            elif target > matrix[row][col]:
                col = -1
            else:
                col -= 1
    
    return [-1, -1]

def __searchInSortedMatrix(matrix, target):
    # Write your code here.
	
	# start in upper right corner
	# if the value == targetValue: return
	# if value > target: col -= 1
	# if value < target: row += 1
    
	row = 0
	col = len(matrix[0])-1
	
	while row < len(matrix) and col >= 0:
		currVal = matrix[row][col]
		
		if currVal == target:
			return [row, col]
		elif currVal > target:
			col -= 1
		else:
			row += 1

	return [-1, -1]
	
## COMPLEXITY
# time -> O(w+h) where h is the height and w is the width of the matrix
# space = O(1)



matrix =  [
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004]
  ]
target =  43

__searchInSortedMatrix(matrix, target)
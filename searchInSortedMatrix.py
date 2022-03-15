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


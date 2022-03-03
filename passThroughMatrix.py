def minimumPassesOfMatrix(matrix):
    # Write your code here.
    passes = 0
    
    noRows = len(matrix)
    noCols = len(matrix[0])
    
    while passes <= noRows*noCols:
        switches, allNegative = passThroughMatrix(matrix)
        if switches == 0: #and not allNegative:
            return passes + 1
        #if allNegative:
        #	return -1
        passes += 1
    
    
    return -1

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

    
if __name__ == "__main__":

    
    matrix = [
        [1, 0, 0, -2, -3],
        [-4, -5, -6, -2, -1],
        [0, 0, 0, 0, -1],
        [1, 2, 3, 0, -2]
    ]

    print(passThroughMatrix(matrix))
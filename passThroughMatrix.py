def minimumPassesOfMatrix(matrix):
    # Write your code here.
    counter = 0 
    noSwitches = 1

    noRows = len(matrix)
    noCols = len(matrix[0])
    
    while noSwitches > 0:
        noSwitches, negatives, positives, zeros = passThroughMatrix(matrix) 
        if positives + zeros == noRows*noCols:
            return counter
        if noSwitches > 0:
            counter += 1

        if noSwitches == 0 and negatives > 0:
            return -1
            
            
    if counter == 0:
        return -1
    
    return counter
    
def passThroughMatrix(matrix):
    # keep track of negative (if there are only negative)
    
    noSwitches = 0
    zeros = 0
    negatives = 0
    positives = 0
    
    noRows = len(matrix)
    noCols = len(matrix[0])
    
    visited = [[False for _ in range(noCols)] for _ in range(noRows)]
    
    for row in range(noRows):
        for col in range(noCols):
            
            if matrix[row][col] < 0:
                negatives += 1
                canSwitch = hasPositiveNeighbor(matrix, row, col, visited)
                if canSwitch:
                    matrix[row][col] = matrix[row][col] * (-1)
                    visited[row][col] = True
                    noSwitches += 1
            elif matrix[row][col] == 0:
                zeros += 1

            else:
                positives += 1

                    
    return noSwitches, negatives, positives,zeros
                    

def hasPositiveNeighbor(matrix, row, col, visited):
    prevCol = col - 1
    nextCol = col + 1
    prevRow = row - 1
    nextRow = row + 1
    
    noRows = len(matrix)
    noCols = len(matrix[0])
    
    if prevCol >= 0 and not visited[row][prevCol] and matrix[row][prevCol] > 0 :
        return True
        
    if nextCol < noCols and not visited[row][nextCol] and matrix[row][nextCol] > 0:
        return True
    
    if prevRow >= 0 and not visited[prevRow][col] and matrix[prevRow][col] > 0:
        return True
    
    if nextRow < noRows and not visited[nextRow][col] and matrix[nextRow][col] > 0:
        return True
    
    return False

    
matrix = [
        [1, 0, 0, -2, -3],
        [-4, -5, -6, -2, -1],
        [0, 0, 0, 0, -1],
        [1, 2, 3, 0, -2]
    ]

print(minimumPassesOfMatrix(matrix))
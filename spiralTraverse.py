array = [
    [1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7]
  ]
res = []
	
arraylen = len(array)

startRow = 0
startColumn = 0

endRow = len(array[0])-1
endColumn = arraylen-1


while startRow <= endRow and startColumn <= endColumn:
    currRow = startRow
    currColumn = startColumn
    
    while currColumn <= endColumn:
        res.append(array[currRow][currColumn])
        currColumn += 1
        
    currRow += 1
    # reset back to range
    currColumn -= 1
    while currRow <= endRow:
        res.append(array[currRow][currColumn])
        currRow += 1
        
    currColumn -= 1    
    # reset back to range
    currRow -= 1
    while currColumn >= startColumn:
        res.append(array[currRow][currColumn])
        currColumn -= 1
        
    currRow -= 1
    # reset back to range
    currColumn += 1
    while currRow > startRow:
        res.append(array[currRow][currColumn])
        currRow -= 1
        
    startRow += 1
    endRow -= 1
    startColumn += 1
    endColumn -= 1

print(res)
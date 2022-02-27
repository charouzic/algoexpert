from array import ArrayType


dif = 10000
arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]
	
arrOneLen = len(arrayOne)
arrTwoLen = len(arrayTwo)

res = [0, 0]
arrayOne.sort()
arrayTwo.sort()

pointerOne = 0
pointerTwo = 0

while pointerOne < arrOneLen and pointerTwo < arrTwoLen:
    firstNum = arrayOne[pointerOne] 
    secondNum = arrayTwo[pointerTwo]
    
    currDiff = abs(firstNum - secondNum)
    
    if currDiff == 0:
        print([firstNum, secondNum])
    
    if dif > currDiff:
        dif = currDiff
        res[0] = firstNum
        res[1] = secondNum
    
    if firstNum < secondNum:
        pointerOne += 1
        
    else:
        pointerTwo += 1
        
print(res)
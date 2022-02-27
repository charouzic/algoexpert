
array = [1, 1, 1, 1, 2]

def hasSingleCycle(array):
    # Write your code here.
	# brute force:
	# create a function that will do the steps based on the given array
	arrLen = len(array)
	counter = arrLen
	
	currIdx = 0
	
	visited = [False for _ in range(len(array))]
	
	while counter > 0:
		visited[currIdx] = True
		currIdx = getIdx(arrLen, array[currIdx], currIdx)
		
		counter -= 1
		
	if False in visited or  currIdx != 0:
		return False
	return True
	
def getIdx(arrayLen, shift, currIdx):
	# 10 + 2 ... len 11
	suma = currIdx + shift
	if suma >= arrayLen:
		return suma % arrayLen
	elif suma < 0:
		return suma%arrayLen
	
	else:
		return suma

print(hasSingleCycle(array))
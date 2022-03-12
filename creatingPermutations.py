def getPermutations(array):
    # Write your code here.
	
	return helperF(0, array, [])

def helperF(i, arr, permutations):
	if i == len(arr)-1:
		permutations.append(arr.copy())
	
	else:
		for j in range(i, len(arr)):
			swap(arr, i, j)
			helperF(i+1, arr, permutations)
			swap(arr, j, i)
	
	return permutations

def swap(array, i, j):
	array[i], array[j] = array[j], array[i]
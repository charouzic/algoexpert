def powerset(array):
    # Write your code here.
	
	powerset = [[]]
	
	for element in array:
		for i in range(len(powerset)):
			curSubset = powerset[i]
			powerset.append(curSubset + [element])
			
	return powerset
			
## Complexity:
# time -> O(n*2^n) where n is the number of elements in the input array
# space -> O(n*2^n)


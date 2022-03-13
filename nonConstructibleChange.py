def nonConstructibleChange(coins):
    # Write your code here.
	noCoins = len(coins)
	if noCoins == 0:
		return 1
	
	sortedCoins = sorted(coins)
	canCreateUpTo = 0
	# 1,1,2,3,5,7,22
	# 1, 2, 4, 7
	# currVal
	# previous sum + current value
	
	for i in range(noCoins):
		currVal = sortedCoins[i]
		
		if currVal > canCreateUpTo + 1:
			return canCreateUpTo + 1
		canCreateUpTo += currVal
		
	return canCreateUpTo + 1
		
## COMPLEXITY
# time: O(n log n) where n is the number of coins in the input array
# space: O(1)


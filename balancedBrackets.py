def balancedBrackets(string):
    # Write your code here.
	
	roundBracket = 0
	squareBracket = 0
	pointyBracket = 0
	
	for i in range(len(string)):
		if string[i] == "(":
			roundBracket += 1
			
		elif string[i] == ")":
			roundBracket -= 1
			
		elif string[i] == "]":
			squareBracket -= 1
			
		elif string[i] == "[":
			squareBracket += 1
			
		elif string[i] == "{":
			pointyBracket += 1
			
		elif string[i] == "}":
			pointyBracket -= 1
			
	return roundBracket == 0 and squareBracket == 0 and pointyBracket == 0

# {[[[[({(}))]]]]}
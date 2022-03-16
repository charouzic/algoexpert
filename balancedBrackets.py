def balancedBrackets(string):
    # Write your code here.
	openingBrackets = "({["
	closingBrackets = "]})"
	opositeBracktes ={
		"(" : ")",
		"[" : "]",
		"{" : "}"
	}
	
	stack = []
	
	for character in string:
		if character in openingBrackets:
			stack.append(character)
		elif character in closingBrackets:
			if len(stack) == 0:
				return False
			bracket = stack.pop()
			if opositeBracktes[bracket] == character:
				pass
			else:
				return False
			
	return len(stack) == 0

string = "{[[[[({(}))]]]]}"

print(balancedBrackets(string))
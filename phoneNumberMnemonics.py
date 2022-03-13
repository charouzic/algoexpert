def phoneNumberMnemonics(phoneNumber):
    # Write your code here.
	letters = {
		0: ["0"],
		1: ["1"],
		2: ["a","b","c"],
		3: ["d","e","f"],
		4: ["g","h","i"],
		5: ["j","k","l"],
		6: ["m","n","o"],
		7: ["p","q","r","s"],
		8: ["t","u","v"],
		9: ["w","x","y","z"]
		
	}
	
	words = letters[phoneNumber[0]]
	
	for i in range(1, len(phoneNumber)):
		
		letters = letters[phoneNumber[i]]
		
		for j in range(len(words)):
			word = words.pop(0)
			for letter in letters:
				words.append(word+letter)
				
	return words


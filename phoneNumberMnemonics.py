def phoneNumberMnemonics(phoneNumber):
    # Write your code here.
	
	mnemonic = ["0" for _ in range(len(phoneNumber))]
	
	return pickCharacter(0, phoneNumber, mnemonic, [])
	

def pickCharacter(idx,phoneNumber, currentMnemonic, res):
	if idx == len(phoneNumber):
		return res.append(''.join(currentMnemonic))
	else:
		listOfLetters = LETTERS[phoneNumber[idx]]
		
		for letter in listOfLetters:
			currentMnemonic[idx] = letter
			pickCharacter(idx + 1, phoneNumber, currentMnemonic, res)
			
	return res

LETTERS = {
		"0": ["0"],
		"1": ["1"],
		"2": ["a","b","c"],
		"3": ["d","e","f"],
		"4": ["g","h","i"],
		"5": ["j","k","l"],
		"6": ["m","n","o"],
		"7": ["p","q","r","s"],
		"8": ["t","u","v"],
		"9": ["w","x","y","z"],
		
	}
	
## COMPLEXITY:
# time -> O(n*4^n) where n is the number of digits in the phone number
# space -> O(n*4^n)
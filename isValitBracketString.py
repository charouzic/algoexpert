def isValidBracketString(string):

    openingBrackets = "([{"
    closingBrackets = ")]}"
    
    opositeBracket = {
        "(": ")",
        "[": "]",
        "{": "}"
    }
    
    brackets = []
    
    for bracket in string:
        if bracket in openingBrackets:
            brackets.append(bracket)
        elif bracket in closingBrackets: 
            if len(brackets) == 0:
                return False
            
            stackBracket = brackets.pop()
            if opositeBracket[stackBracket] != bracket:
                return False
                
    
    return len(brackets) == 0


string = "([])(){}(())()()"

str2 = "(((((({{{{{[[[[[([)])]]]]]}}}}}))))))"

str3 = "(141[])(){waga}((51afaw))()hh()"

print(isValidBracketString(str3))
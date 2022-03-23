def validIPAddresses(string):
    # Write your code here.
    # I need to assign 4 dots across the string
    validParts = []

    for i in range(len(string)):
        currNumber = string[i]
        while currNumber != "00" and int(currNumber) <= 255:
            validParts.append(currNumber)
            if i+1 < len(string):
                currNumber += string[i+1]
            else:
                currNumber = "00"

    return validParts
        
string = "1921680"

print(validIPAddresses(string))
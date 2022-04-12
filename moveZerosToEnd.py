def moveZerosToTheEnd(string):
    left = 0
    right = len(string) - 1

    string = list(string)

    while left < right:
        while left < right and string[left] != "0":
            print(string[left])
            left += 1

        while right > left and string[right] == "0":
            right -= 1
        
        if left < right:
            string[left], string[right] = string[right], string[left]
            left += 1
            right -= 1

    return string

string = "000acacsc"

string2 = "00a000"

#string[0], string[6] = string[6], string[0] 

#print(string)
print(moveZerosToTheEnd(string2))

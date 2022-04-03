def longestSubstringWithoutDuplication(string):
    # Write your code here.
    # bruteforce
    longest = 0
    stringRange = (0,0)
    finishIdx = 0
    
    for i in range(len(string)):
        d = {}
        count = 0
        idx = i
        while idx < len(string):
            currLetter = string[idx]
            if currLetter not in d:
                d[currLetter] = 1
                count += 1
                idx += 1
            else:
                idx = len(string)
                
        
        if count > longest:
            longest = count
            stringRange = (i, i+count)
                
    return string[stringRange[0]:stringRange[1]]

## COMPLEXITY
# time: O() where n is the number of characters in the input string
# space: O(n)
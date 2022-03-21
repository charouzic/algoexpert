def longestPalindromicSubstring(string):
    # Write your code here.
    
    # get all substrings
    
    longestPalindrom = ""
    
    for i in range(len(string)):
        for j in range(len(string)):
            substring = ""
            beginning = i
            while beginning <= j:
                substring += string[beginning]
                beginning += 1
            
            currPlaindrom = palindrom(substring)
            
            if len(currPlaindrom) > len(longestPalindrom):
                longestPalindrom = currPlaindrom
                
    
    return longestPalindrom
                


def palindrom(string):
    strLen = len(string)
    
    beginning = 0
    end  =  len(string) - 1
    
    while beginning <= end:
        if string[beginning] != string[end]:
            return ""
        beginning += 1
        end -= 1
        
    return string
        
        
print(longestPalindromicSubstring("abaxyzyxf"))
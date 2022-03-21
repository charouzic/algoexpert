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

def longestPalindromicSubstring(string):
    # Write your code here.
    longestPlaindrom = ""
    
    for i in range(len(string)):
        # index i is the middle
        
        substring1 = getPalindrom(string, i - 1, i + 1)
        
        substring2 = getPalindrom(string, i - 1, i)
        
        if len(substring1) > len(substring2):
            substring = substring1
        else:
            substring = substring2
        
        
        if len(substring) > len(longestPlaindrom):
            longestPlaindrom = substring
            
    return longestPlaindrom
            
        
def getPalindrom(string, left, right):
    
    while right < len(string) and left >= 0:
        if string[left] != string[right]:
            break
        else:
            left -= 1
            right += 1
            
    return string[left + 1 : right]
    
## COMPLEXITY
# time: O(n^2) where n is the number of characters in the string
# space: O(n)
        
        
print(longestPalindromicSubstring("abaxyzyxf"))
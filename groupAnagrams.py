def groupAnagrams(words):
    # Write your code here.
    alphabeticallyOrderedStrings = {}
    result = []
    
    for i in range(len(words)):
        sortedChars = ''.join(sorted(words[i]))
        if sortedChars in alphabeticallyOrderedStrings:
            alphabeticallyOrderedStrings[sortedChars].append(words[i])
        else:
            alphabeticallyOrderedStrings[sortedChars] = [words[i]]
        
    for l in alphabeticallyOrderedStrings.keys():
        
        result.append(alphabeticallyOrderedStrings[l])

    return result

## COMPLEXITY
# time -> O(w * n * log(n)) where n is the number of letters in the longest word and w is the number of words in the input
# space -> O(w * n)
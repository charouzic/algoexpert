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
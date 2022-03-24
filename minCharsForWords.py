def minimumCharactersForWords(words):
    # Write your code here.
    result = []
    characters = {}
    for word in words:
        w = {}
        for letter in word:
            if letter not in w:
                w[letter] = 1
            else:
                w[letter] += 1
        for l in w.keys():
            if not l in characters:
                characters[l] = w[l]
            else:
                characters[l] = max(characters[l], w[l])
                
    for i in characters.keys():
        for _ in range(characters[i]):
            result.append(i)
            
    return result

## COMPLEXITY
# time --> O(w * l) where w is the number of words in the input and l is the number of letters in the longest word
# space --> O(c) where c is the number of unique letters in the input words

words = ["this", "that", "did", "deed", "them!", "a"]

minimumCharactersForWords(words)
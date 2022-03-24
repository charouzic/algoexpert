def minimumCharactersForWords(words):
    # Write your code here.
    result = []
    characters = {}
    for word in words:
        word = {}
        for letter in word:
            if letter not in characters:
                word[letter] = 1
            else:
                word[letter] += 1
        for l in word.keys():
            if not l in characters:
                characters[l] = word[l]
            else:
                characters[l] = max(characters[l], word[l])
                
    for i in characters.keys():
        for _ in range(characters[i]):
            result.append(i)
            
    return result
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

words = ["this", "that", "did", "deed", "them!", "a"]

minimumCharactersForWords(words)
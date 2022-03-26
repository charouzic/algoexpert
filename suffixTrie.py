# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        # Write your code here.
        
        for idx in range(len(string)):
            self.insertSubstring(idx, string)
            
    
    def insertSubstring(self, i, string):
        currNode = self.root
        for j in range(i, (len(string))):
            letter = string[j]
            if letter not in currNode:
                currNode[letter] = {}
            currNode = currNode[letter]	
            
        currNode[self.endSymbol] = True
            
            
    def contains(self, string):
        # Write your code here.
        currNode = self.root
        
        for letter in string:
            if letter not in currNode:
                return False
            currNode = currNode[letter]
        
        return self.endSymbol in currNode 
        


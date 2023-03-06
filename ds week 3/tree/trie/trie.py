class Node:
    def __init__(self):
        self.children ={}
        self.endofword = False
class Trie:
    def __init__(self):
        self.root = Node()
    def insert(self,word):
        ptr = self.root
        for letter in word:
            if letter not in ptr.children:
                ptr.children[letter] = Node()
            ptr = ptr.children[letter]
        ptr.endofword = True
    def search(self,word):
        ptr = self.root
        for letter in word:
            if letter not in ptr.children:
                return False
            ptr = ptr.children[letter]
        if ptr.endofword:
            return True
        else:
            return False
    def startWith(self,prefix):
        ptr = self.root
        for letter in prefix:
            if letter not in ptr.children:
                return False
            ptr = ptr.children[letter]
        return True

# create a new Trie object
trie = Trie()

# insert some words into the Trie
trie.insert('apple')
trie.insert('banana')
trie.insert('cherry')
trie.insert('dog')

# search for a word in the Trie
print(trie.search('banana'))  # True
print(trie.search('cat'))     # False

# check if there are any words in the Trie that start with a prefix
print(trie.startWith('a'))    # True
print(trie.startWith('z'))    # False


        
        
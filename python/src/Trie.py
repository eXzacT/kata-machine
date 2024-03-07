''' A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. 
    There are various applications of this data structure, such as autocomplete and spellchecker.

    Implement the Trie class:

        Trie() Initializes the trie object.
        
        void insert(String word) Inserts the 'word' into the trie.
        
        boolean search(String word) Returns true if 'word' is in the trie (i.e., was inserted before), and false otherwise.
        
        boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the 'prefix', and false otherwise.'''


class Node:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def __repr__(self) -> str:
        return f"Node({self.children}), isWord={self.isWord}"


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()

            curr = curr.children[c]

        curr.isWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False

            curr = curr.children[c]

        return curr.isWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False

            curr = curr.children[c]

        return True

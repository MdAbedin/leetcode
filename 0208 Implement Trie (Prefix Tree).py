class Node:
    def __init__(self, val = None):
        self.val = val
        self.children = [None]*26

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root
        i = 0
        
        while i < len(word) and cur.children[ord(word[i]) - ord('a')]:
            cur = cur.children[ord(word[i]) - ord('a')]
            i += 1
            
        while i < len(word):
            cur.children[ord(word[i]) - ord('a')] = Node()
            cur = cur.children[ord(word[i]) - ord('a')]
            i += 1
            
        cur.val = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.root.children[ord(word[0]) - ord('a')]
        i = 1
        
        while i < len(word) and cur:
            cur = cur.children[ord(word[i]) - ord('a')]
            i += 1
            
        return cur and cur.val
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.root.children[ord(prefix[0]) - ord('a')]
        i = 1
        
        while i < len(prefix) and cur:
            cur = cur.children[ord(prefix[i]) - ord('a')]
            i += 1
            
        return cur is not None

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

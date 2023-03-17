class Trie:
    def __init__(self):
        self.trie = [False,{}]

    def get_node(self, word, create):
        node = self.trie

        for c in word:
            if c not in node[1]:
                if create: node[1][c] = [False,{}]
                else: return None

            node = node[1][c]

        return node

    def insert(self, word: str) -> None:
        self.get_node(word,True)[0] = True

    def search(self, word: str) -> bool:
        return (node := self.get_node(word,False)) and node[0]

    def startsWith(self, prefix: str) -> bool:
        return self.get_node(prefix,False)

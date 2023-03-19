class WordDictionary:
    def __init__(self):
        self.trie = [False,{}]

    def addWord(self, word: str) -> None:
        node = self.trie

        for c in word:
            if c not in node[1]: node[1][c] = [False,{}]
            node = node[1][c]

        node[0] = True

    def search(self, word: str) -> bool:
        bfs = deque([self.trie])

        for c in word:
            for i in range(len(bfs)):
                cur = bfs.popleft()

                if c == ".": bfs.extend(cur[1].values())
                else:
                    if c in cur[1]: bfs.append(cur[1][c])

        return any(node[0] for node in bfs)

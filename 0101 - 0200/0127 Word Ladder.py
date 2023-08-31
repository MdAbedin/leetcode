class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words_set = set(wordList)
        g = {word: [new_word for i,c in product(range(len(word)),ascii_lowercase) if c != word[i] and (new_word := word[:i]+c+word[i+1:]) in words_set] for word in wordList+[beginWord]}

        bfs = deque([beginWord])
        seen = {beginWord}
        length = 2

        while bfs:
            for i in range(len(bfs)):
                word = bfs.popleft()

                for word2 in g[word]:
                    if word2 == endWord: return length

                    if word2 not in seen:
                        seen.add(word2)
                        bfs.append(word2)

            length += 1
        
        return 0

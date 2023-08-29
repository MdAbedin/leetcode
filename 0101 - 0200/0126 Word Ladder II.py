class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList: return []

        wordList += [beginWord]
        g = {word: [word2 for word2 in wordList if sum(c1!=c2 for c1,c2 in zip(word,word2))==1] for word in wordList}

        dists_from_end = defaultdict(lambda: inf, {endWord:0})
        bfs = deque([endWord])
        dist = 1

        while bfs:
            for i in range(len(bfs)):
                word = bfs.popleft()

                for word2 in g[word]:
                    if word2 not in dists_from_end:
                        dists_from_end[word2] = dist
                        bfs.append(word2)

            dist += 1

        bfs = deque([[beginWord]])
        ans = []

        while bfs:
            for i in range(len(bfs)):
                sequence = bfs.popleft()

                for new_word in g[sequence[-1]]:
                    if dists_from_end[new_word] != dists_from_end[sequence[-1]]-1 or new_word in sequence: continue

                    new_sequence = sequence + [new_word]

                    if new_word == endWord: ans.append(new_sequence)
                    else: bfs.append(new_sequence)

        return ans

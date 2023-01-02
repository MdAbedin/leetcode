class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = [False,{}]

        for word in words:
            cur_node = trie

            for letter in word:
                if letter not in cur_node[1]: cur_node[1][letter] = [False,{}]
                cur_node = cur_node[1][letter]

            cur_node[0] = True

        bfs = deque([[trie,""]])
        ans = ""

        while bfs:
            cur_node,cur_string = bfs.popleft()
            if len(cur_string) > len(ans) or (len(cur_string) == len(ans) and cur_string < ans): ans = cur_string

            for letter,nei_node in cur_node[1].items():
                if nei_node[0]: bfs.append([nei_node, cur_string+letter])

        return ans

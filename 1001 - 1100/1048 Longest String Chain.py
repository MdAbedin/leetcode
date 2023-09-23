class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        @cache
        def solve(word): return 1 + max((solve(word2) for word2 in words if len(word2) == len(word)+1 and (word2.startswith(word) or any(word2 == word[:i]+word2[i]+word[i:] for i in range(len(word))))),default=0)

        return max(map(solve,words))

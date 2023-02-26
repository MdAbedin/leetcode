class Solution:
    @cache
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 or not word2: return max(len(word1), len(word2))
        return min(self.minDistance(word1[:-1], word2[:-1]) + (1 if word1[-1] != word2[-1] else 0), 1 + self.minDistance(word1[:-1], word2), 1+ self.minDistance(word1, word2[:-1]))

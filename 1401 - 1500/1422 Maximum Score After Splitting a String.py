class Solution:
    def maxScore(self, s: str) -> int:
        return max(s[:i+1].count("0")+s[i+1:].count("1") for i in range(len(s)-1))

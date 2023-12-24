class Solution:
    def minOperations(self, s: str) -> int:
        return min(sum(c != str(i%2) for i,c in enumerate(s)),sum(c == str(i%2) for i,c in enumerate(s)))

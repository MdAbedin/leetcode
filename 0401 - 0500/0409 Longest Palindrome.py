class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        return sum(c//2 for c in counts.values())*2 + any(c%2 == 1 for c in counts.values())

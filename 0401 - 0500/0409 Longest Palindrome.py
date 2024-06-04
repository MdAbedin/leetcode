class Solution:
    def longestPalindrome(self, s: str) -> int:
        return sum(c-c%2 for c in Counter(s).values())+any(c%2 == 1 for c in Counter(s).values())

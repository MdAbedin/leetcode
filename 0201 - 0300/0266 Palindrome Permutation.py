class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        return sum(c%2 == 1 for c in Counter(s).values()) <= 1

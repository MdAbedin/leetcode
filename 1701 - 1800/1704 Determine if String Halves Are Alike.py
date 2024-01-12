class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        return sum(c in "aeiou" for c in s[:len(s)//2].lower()) == sum(c in "aeiou" for c in s[len(s)//2:].lower())

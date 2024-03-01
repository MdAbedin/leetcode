class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        return "".join([c2 for c2 in s if c2.isalpha()][~sum(map(str.isalpha,s[:i]))] if c.isalpha() else c for i,c in enumerate(s))

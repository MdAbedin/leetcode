class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        for c in s: i += i < len(t) and c == t[i]
        return len(t)-i

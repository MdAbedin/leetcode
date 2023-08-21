class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return any(all(s[i] == s[i%length] for i in range(len(s))) for length in range(1,len(s)) if len(s)%length == 0)

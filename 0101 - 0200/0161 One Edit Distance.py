class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        for i,c1,c2 in zip(range(len(s)),s,t):
            if c1 != c2: return s[i:] == t[i+1:] or s[i+1:] == t[i:] or s[i+1:] == t[i+1:]
        
        return abs(len(s)-len(t)) == 1

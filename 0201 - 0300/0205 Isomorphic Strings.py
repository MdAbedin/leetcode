class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m1,m2 = {},{}

        for c1,c2 in zip(s,t):
            if m1.setdefault(c1,c2) != c2 or m2.setdefault(c2,c1) != c1: return False

        return True

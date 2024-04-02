class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m1,m2 = {},{}
        return all(m1.setdefault(c1,c2) == c2 and m2.setdefault(c2,c1) == c1 for c1,c2 in zip(s,t))

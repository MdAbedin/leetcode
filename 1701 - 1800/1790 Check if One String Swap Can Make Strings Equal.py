class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        return s1 == s2 or any(s1[:i1]+s1[i2]+s1[i1+1:i2]+s1[i1]+s1[i2+1:] == s2 for i1 in range(len(s1)) for i2 in range(i1+1,len(s1)))

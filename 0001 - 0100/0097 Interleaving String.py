class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @cache
        def solve(s1,s2,s3):
            if not s1 or not s2 or not s3: return s1+s2 == s3
            return (s1[0] == s3[0] and solve(s1[1:],s2,s3[1:])) or (s2[0] == s3[0] and solve(s1,s2[1:],s3[1:]))

        return solve(s1,s2,s3)
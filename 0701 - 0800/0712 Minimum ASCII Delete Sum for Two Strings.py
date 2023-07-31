class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        @cache
        def solve(s1,s2):
            if not s1 or not s2: return sum(map(ord,s1))+sum(map(ord,s2))
            if s1[-1] == s2[-1]: return solve(s1[:-1],s2[:-1])
            return min(ord(s1[-1])+solve(s1[:-1],s2),ord(s2[-1])+solve(s1,s2[:-1]))

        return solve(s1,s2)

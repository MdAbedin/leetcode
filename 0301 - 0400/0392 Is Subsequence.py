class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        def solve(i1,i2):
            if i1 == len(s): return True
            if i2 == len(t): return False
            return solve(i1+1,i2+1) if s[i1] == t[i2] else solve(i1,i2+1)

        return solve(0,0)

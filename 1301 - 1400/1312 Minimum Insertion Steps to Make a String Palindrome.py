class Solution:
    def minInsertions(self, s: str) -> int:
        @cache
        def solve(l,r):
            if r-l+1 <= 1: return 0
            return solve(l+1,r-1) if s[l] == s[r] else min(solve(l+1,r),solve(l,r-1))+1

        return solve(0,len(s)-1)

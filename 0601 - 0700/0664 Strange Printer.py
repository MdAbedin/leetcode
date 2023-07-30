class Solution:
    def strangePrinter(self, s: str) -> int:
        @cache
        def solve(l,r): return 1 if l == r else min(solve(l,i)+solve(i+1,r) for i in range(l,r)) - (1 if s[l] == s[r] else 0)
        return solve(0,len(s)-1)

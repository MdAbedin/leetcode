class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def solve(i): return 1 if i == len(s) else sum(solve(i+len(str(num))) for num in range(1,27) if s.startswith(str(num),i))
        return solve(0)

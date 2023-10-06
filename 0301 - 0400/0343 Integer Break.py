class Solution:
    def integerBreak(self, n: int) -> int:
        @cache
        def solve(num): return 1 if num <= 1 else max(x*solve(num-x) for x in range(1,num+(num!=n)))
        return solve(n)

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        m = 10**9+7

        @cache
        def solve(l):
            if l < 0: return 0
            if l == 0: return 1
            return (solve(l-zero)+solve(l-one))%m

        return sum(solve(l) for l in range(low,high+1))%m

class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 10**9+7

        @cache
        def solve(num): return 1 if num == 1 else ((2*num-1)*(2*num)//2 * solve(num-1))%MOD

        return solve(n)

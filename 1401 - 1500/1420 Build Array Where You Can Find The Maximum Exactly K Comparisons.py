class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9+7

        @cache
        def solve(i,m,k): return k == 1 if i == 0 else (solve(i-1,m,k)*m + sum(solve(i-1,m2,k-1) for m2 in range(1,m)))%MOD

        return sum(solve(n-1,x,k) for x in range(1,m+1))%MOD

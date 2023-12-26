class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        @cache
        def solve(n,target): return target == 0 if n == 0 else sum(solve(n-1,target-x) for x in range(1,k+1))%(10**9+7)
        return solve(n,target)

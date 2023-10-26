class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10**9+7
        nums_set = set(arr)

        @cache
        def solve(x): return (1+sum(solve(num)*solve(x//num) for num in arr if x%num == 0 and x//num in nums_set))%MOD

        return sum(solve(x) for x in arr)%MOD

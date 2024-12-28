class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        ps = [0]+list(accumulate(nums))
        
        @cache
        def solve(i,c): return [] if i >= len(nums)-k+1 or c == 0 else max([i]+solve(i+k,c-1),solve(i+1,c),key = lambda l: sum(ps[i2+k]-ps[i2] for i2 in l))
        
        return solve(0,3)

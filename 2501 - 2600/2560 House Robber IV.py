class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        return bisect_left(range(10**9+1),True,key = lambda x: sum(ceil(len(list(g))/2) for b,g in groupby(nums,key = lambda num: num <= x) if b) >= k)

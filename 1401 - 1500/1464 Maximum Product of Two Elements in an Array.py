class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        return (sorted(nums)[-1]-1)*(sorted(nums)[-2]-1)

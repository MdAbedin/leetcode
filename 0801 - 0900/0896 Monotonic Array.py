class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        return nums in [sorted(nums),sorted(nums,reverse=True)]

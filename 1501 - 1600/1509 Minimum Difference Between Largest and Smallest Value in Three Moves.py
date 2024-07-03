class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        return 0 if len(nums) <= 4 else min(nums[~(3-i)]-nums[i] for i in range(4))

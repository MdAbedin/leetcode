class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        return max(bisect_right(nums,nums[i]+2*k)-i for i in range(len(nums)))

class Solution:
    def check(self, nums: List[int]) -> bool:
        return any(nums[i:]+nums[:i] == sorted(nums[i:]+nums[:i]) for i in range(len(nums)))

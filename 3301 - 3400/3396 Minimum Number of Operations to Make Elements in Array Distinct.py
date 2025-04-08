class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return next(i for i in range(0,len(nums)+2,3) if len(set(nums[i:])) == len(nums[i:]))//3

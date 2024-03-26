class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for num in nums:
            while num in range(1,len(nums)+1) and nums[num-1] != num: nums[num-1],num = num,nums[num-1]

        return next((i+1 for i,num in enumerate(nums) if num != i+1),len(nums)+1)

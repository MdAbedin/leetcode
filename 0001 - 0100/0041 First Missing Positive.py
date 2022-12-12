class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while 1 <= nums[i] <= len(nums) and nums[i] != nums[nums[i]-1]:
                other_index = nums[i]-1
                nums[i], nums[other_index] = nums[other_index], nums[i]
                
        for i in range(len(nums)):
            if nums[i] != i+1: return i+1
            
        return len(nums)+1

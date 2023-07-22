class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        next_i = 2

        for i in range(2,len(nums)):
            if nums[i] != nums[next_i-2]:
                nums[next_i],nums[i] = nums[i],nums[next_i]
                next_i += 1

        return next_i

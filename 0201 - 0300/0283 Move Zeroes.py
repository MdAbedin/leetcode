class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0

        for i2 in range(len(nums)):
            if nums[i2] != 0:
                nums[i],nums[i2] = nums[i2],nums[i]
                i += 1

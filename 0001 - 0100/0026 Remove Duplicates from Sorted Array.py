class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i1 = 0

        for i2 in range(len(nums)):
            if i2 == 0 or nums[i2-1] != nums[i2]:
                nums[i1] = nums[i2]
                i1 += 1

        return i1

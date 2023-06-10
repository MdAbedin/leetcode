class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        end = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[end] = nums[i]
                end += 1

        return end

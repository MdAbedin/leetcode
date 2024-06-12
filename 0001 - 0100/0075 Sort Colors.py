class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i0,i1 = 0,0

        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i0],nums[i] = nums[i],nums[i0]
                i0 += 1
                i1 = max(i1,i0)

            if nums[i] == 1:
                nums[i1],nums[i] = nums[i],nums[i1]
                i1 += 1

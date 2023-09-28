class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[-1] == nums[0]:
            ans = nums[-1]

            for num in reversed(nums):
                if num > ans: return ans
                ans = num

        return nums[bisect_left(nums,True,key=lambda num: num <= nums[-1])]

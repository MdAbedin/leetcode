class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1

        while l <= r:
            m = (l+r)//2

            if m-1 >= 0 and nums[m-1] == nums[m]:
                first_i = m-1
            elif m+1 < len(nums) and nums[m+1] == nums[m]:
                first_i = m
            else:
                return nums[m]

            if first_i % 2 == 0:
                l = m+1
            else:
                r = m-1

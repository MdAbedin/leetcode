class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums = [-inf]+nums+[-inf]
        return bisect_left(range(1,len(nums)-1),0,key = lambda i: -1 if nums[i] < nums[i+1] else (1 if nums[i-1] > nums[i] else 0))

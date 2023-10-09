class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l,r = bisect_left(nums,target),bisect_right(nums,target)-1
        return [-1,-1] if l == len(nums) or nums[l] != target else [l,r]

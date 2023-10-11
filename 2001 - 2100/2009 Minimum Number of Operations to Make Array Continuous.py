class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums2 = sorted(set(nums))
        return min(len(nums)-(bisect_right(nums2,num+len(nums)-1)-i) for i,num in enumerate(nums2))

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return [l*r for l,r in zip([1]+list(accumulate(nums[:-1],mul)), list(accumulate(nums[:0:-1],mul))[::-1]+[1])]

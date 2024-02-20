class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return reduce(xor,range(len(nums)+1)) ^ reduce(xor,nums)

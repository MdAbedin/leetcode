class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        return max(len(list(takewhile(lambda i2: not reduce(or_,nums[i:i2],0)&nums[i2], range(i,len(nums))))) for i in range(len(nums)))

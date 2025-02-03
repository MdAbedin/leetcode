class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        return max(l for l in range(1,len(nums)+1) if any(len(set(nums[i:i+l])) == l and nums[i:i+l] in [sorted(nums[i:i+l]),sorted(nums[i:i+l],reverse=True)] for i in range(len(nums)-l+1)))

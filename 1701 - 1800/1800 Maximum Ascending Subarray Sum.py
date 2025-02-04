class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        return max(sum(nums[i:i2+1]) for i in range(len(nums)) for i2 in range(i,len(nums)) if all(a < b for a,b in pairwise(nums[i:i2+1])))

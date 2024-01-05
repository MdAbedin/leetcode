class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @cache
        def solve(i): return 0 if i == len(nums) else 1+max(solve(i2) for i2 in range(i+1,len(nums)+1) if i2 == len(nums) or nums[i] < nums[i2])
        return max(map(solve,range(len(nums))))

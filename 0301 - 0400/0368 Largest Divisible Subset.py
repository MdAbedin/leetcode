class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()

        @cache
        def solve(i): return [nums[i]] + max((solve(i2) for i2 in range(i+1,len(nums)) if nums[i2]%nums[i] == 0),default=[],key=len)

        return max(map(solve,range(len(nums))),key=len)

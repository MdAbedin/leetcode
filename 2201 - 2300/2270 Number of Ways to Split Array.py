class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        s = sum(nums)
        ps = ans = 0

        for num in nums[:-1]:
            ps += num
            ans += ps >= s-ps

        return ans

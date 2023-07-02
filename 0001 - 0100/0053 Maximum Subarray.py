class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -inf
        s = -inf

        for num in nums:
            s = max(s+num,num)
            ans = max(ans,s)

        return ans

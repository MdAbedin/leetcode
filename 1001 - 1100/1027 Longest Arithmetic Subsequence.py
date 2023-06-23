class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = defaultdict(lambda: 1)

        for i,num in enumerate(nums):
            for j,prev_num in enumerate(nums[:i]):
                dp[i,num-prev_num] = dp[j,num-prev_num]+1

        return max(dp.values())

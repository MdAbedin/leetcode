class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = [[[0,-inf] for i2 in range(k+1)] for i in range(len(prices))]
        dp[0][0][1] = -prices[0]

        for i in range(1,len(prices)):
            for i2 in range(k+1):
                if i2 >= 1: dp[i][i2][0] = max(dp[i-1][i2][0],dp[i-1][i2-1][1]+prices[i])
                dp[i][i2][1] = max(dp[i-1][i2][1],dp[i-1][i2][0]-prices[i])

        return max(dp[-1][i][0] for i in range(k+1))

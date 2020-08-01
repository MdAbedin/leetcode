class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        
        dp = [0]*len(prices)
        dp2 = [0]*len(prices)
        
        for i in range(len(prices)-2,-1,-1):
            for j in range(len(prices)-1, i, -1):
                dp[i] = max(dp[i], prices[j]-prices[i] + (dp2[j+2] if j+2<len(prices) else 0))
                dp2[i] = max(dp2[i+1], dp[i])
                
        return dp2[0]

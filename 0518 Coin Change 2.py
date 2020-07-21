class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1]+[0]*(amount)
        dp2= [1]+[0]*(amount)
        coins = set(coins)
        
        for val in coins:
            for i in range(amount+1):
                dp2[i] += 0 if i-val < 0 else dp[i-val]
                dp2[i] += 0 if i-val <=0 else dp2[i-val]-dp[i-val]
                
            dp = dp2
            
        return dp[-1]

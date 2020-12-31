dp = {0:0,1:1,2:2}

class Solution:
    def minDays(self, n: int) -> int:
        if n in dp: return dp[n]
        
        ans = 1 + min(n%2 + self.minDays((n-n%2)//2), n%3 + self.minDays((n-n%3)//3))
        dp[n] = ans
        
        return ans

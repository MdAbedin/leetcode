class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9+7
        dp = [1] + [0]*min(steps,arrLen-1)

        for _ in range(steps):
            dp2 = dp[:]
            
            for i in range(len(dp)):
                if i-1 >= 0: dp2[i-1] += dp[i]
                if i+1 < len(dp): dp2[i+1] += dp[i]

            dp = [num % MOD for num in dp2]

        return dp[0]

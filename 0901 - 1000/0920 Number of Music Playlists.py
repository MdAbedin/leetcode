class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = 10**9+7
        dp = [1]+[0]*n

        for i in range(1,goal+1):
            dp2 = [0]*(n+1)

            for i2 in range(1,n+1):
                if i > k+1: dp2[i2] += dp[i2]*(n-i2+1) + dp[i2-1]*(i2-k-1)
                else: dp2[i2] += dp[i2-1]*(n-i2+1)
                dp2[i2] %= MOD

            dp = dp2

        return dp[n]

class Solution:
    def checkRecord(self, n: int) -> int:
        mod = 10**9+7
        dp = [[1,0,0],[0,0,0]]

        for i in range(n):
            dp2 = [[0,0,0],[0,0,0]]

            for a in range(2):
                for l in range(3):
                    if a+1 < 2:
                        dp2[a+1][0] += dp[a][l]
                        dp2[a+1][0] %= mod

                    if l+1 < 3:
                        dp2[a][l+1] += dp[a][l]
                        dp2[a][l+1] %= mod

                    dp2[a][0] += dp[a][l]
                    dp2[a][0] %= mod

            dp = dp2

        return sum(map(sum,dp))%mod

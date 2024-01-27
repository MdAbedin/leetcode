class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9+7
        dp = [1]+[0]*k

        for l in range(n):
            dp2 = [0]*(k+1)
            s = 0

            for i in range(k+1):
                s += dp[i]
                dp2[i] = s
                if i-l >= 0: s -= dp[i-l]

            dp = dp2

        return dp[-1]%MOD

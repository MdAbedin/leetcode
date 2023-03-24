class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9+7
        dp = [1] + [0]*k

        for size in range(2,n+1):
            dp2 = [0]*(k+1)
            
            for i,num in enumerate(dp):
                dp2[i] += num
                if i+size < len(dp2): dp2[i+size] -= num

            dp = list(map(lambda x: x%MOD, accumulate(dp2)))

        return dp[k]

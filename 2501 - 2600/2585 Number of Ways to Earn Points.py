class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        MOD = 10**9+7
        dp = [0]*(target+1)
        dp[0] = 1
        
        for count,points in types:
            dp2 = dp[:]
            
            for i in range(len(dp)):
                for uses in range(1,count+1):
                    if i+uses*points < len(dp):
                        dp2[i+uses*points] += dp[i]
                        dp2[i+uses*points] %= MOD
                    else:
                        break
                        
            dp = dp2
        
        return dp[target]

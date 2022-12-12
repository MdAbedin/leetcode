class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        A.sort()
        nums = set(A)
        dp = [1]*len(A)
        ans = 0
        
        for i in range(len(A)):
            for j in range(i):
                if A[i]/A[j] in nums:
                    dp[i] += dp[j] * dp[A.index(A[i]//A[j])]
                    dp[i] = int(dp[i] % (1e9+7))
            
            ans += dp[i]
            ans = int(ans % (1e9+7))
        
        return ans

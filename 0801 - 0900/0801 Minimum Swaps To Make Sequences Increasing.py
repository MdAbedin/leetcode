class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        dp = [[float('inf'),float('inf')] for i in range(len(A))]
        dp[0] = [0,1]

        for i in range(1,len(A)):
            if A[i] > A[i-1] and B[i] > B[i-1]:
                dp[i][0] = min(dp[i][0], dp[i-1][0])
                dp[i][1] = min(dp[i][1], dp[i-1][1]+1)

            if B[i] > A[i-1] and A[i] > B[i-1]:
                dp[i][1] = min(dp[i][1], dp[i-1][0]+1)
                dp[i][0] = min(dp[i][0], dp[i-1][1])
        
        return min(dp[-1])

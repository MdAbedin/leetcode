class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp = [0]*len(matrix[0])
        for row in matrix: dp = [row[i] + min(dp[i-1] if i-1 >= 0 else inf,dp[i],dp[i+1] if i+1 < len(matrix[0]) else inf) for i in range(len(matrix[0]))]
        return min(dp)

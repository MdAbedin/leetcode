class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = list(accumulate(grid[0]))

        for r in range(1,len(grid)):
            for c in range(len(grid[0])):
                dp[c] = grid[r][c] + min(dp[c], dp[c-1] if c-1 >= 0 else inf)

        return dp[-1]

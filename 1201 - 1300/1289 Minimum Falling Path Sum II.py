class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        @cache
        def solve(r,c): return 0 if r == len(grid) else min(grid[r][c2]+solve(r+1,c2) for c2 in range(len(grid[0])) if c2 != c)
        return solve(0,-1)

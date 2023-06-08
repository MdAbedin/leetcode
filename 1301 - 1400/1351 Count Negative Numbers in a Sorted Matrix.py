class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        R,C = len(grid),len(grid[0])
        c = 0
        ans = 0

        for r in range(R-1,-1,-1):
            while c < C and grid[r][c] >= 0: c += 1
            ans += C-c

        return ans

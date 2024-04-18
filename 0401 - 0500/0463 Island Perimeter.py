class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        return sum(sum(r2 not in range(len(grid)) or c2 not in range(len(grid[0])) or grid[r2][c2] == 0 for r2,c2 in [[r+1,c],[r-1,c],[r,c+1],[r,c-1]]) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == 1)

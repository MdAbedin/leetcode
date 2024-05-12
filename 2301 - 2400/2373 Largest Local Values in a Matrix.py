class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        return [[max(grid[r2][c2] for r2 in range(r-1,r+2) for c2 in range(c-1,c+2)) for c in range(1,len(grid[0])-1)] for r in range(1,len(grid)-1)]

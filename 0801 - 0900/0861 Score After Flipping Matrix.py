class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        grid2 = [[1-x for x in row] if row[0] == 0 else row for r,row in enumerate(grid)]
        grid3 = [[1]+[1-x for x in row[1:]] if row[0] == 1 else [1]+row[1:] for r,row in enumerate(grid)]
        return max(sum(max(col.count(0),col.count(1))*(2**(len(grid[0])-c-1)) for c,col in enumerate(zip(*grid))) for grid in [grid2,grid3])

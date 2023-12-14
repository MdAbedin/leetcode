class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        R,C = len(grid),len(grid[0])
        rows,cols = list(map(sum,grid)),list(map(sum,zip(*grid)))

        return [[2*(rows[r]+cols[c])-(R+C) for c in range(C)] for r in range(R)]

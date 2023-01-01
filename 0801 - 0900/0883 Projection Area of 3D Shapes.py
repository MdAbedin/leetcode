class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        return sum(height>0 for row in grid for height in row) + sum(map(max,grid)) + sum(map(max,zip(*grid)))

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if y == 0 and x == 0:
                    continue
                if y-1 >= 0 and x-1 >= 0:
                    grid[y][x] += min(grid[y-1][x], grid[y][x-1])
                elif y-1 >= 0:
                    grid[y][x] += grid[y-1][x]
                else:
                    grid[y][x] += grid[y][x-1]
                
        return grid[-1][-1]

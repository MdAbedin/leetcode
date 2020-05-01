class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0
        if not obstacleGrid[0]:
            return 1
        
        if obstacleGrid[0][0] == 1:
            return 0
        
        for y in range(len(obstacleGrid)):
            for x in range(len(obstacleGrid[0])):
                if y == 0 and x == 0:
                    obstacleGrid[0][0] = 1
                    continue
                    
                if obstacleGrid[y][x] == 0:
                    if y-1 >= 0 and obstacleGrid[y-1][x] >= 0:
                        obstacleGrid[y][x] += obstacleGrid[y-1][x]
                    if x-1 >= 0 and obstacleGrid[y][x-1] >= 0:
                        obstacleGrid[y][x] += obstacleGrid[y][x-1]
                else:
                    obstacleGrid[y][x] = -1
        
        return obstacleGrid[-1][-1] if obstacleGrid[-1][-1] >= 0 else 0

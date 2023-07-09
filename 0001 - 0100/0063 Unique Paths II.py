class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [1] + [0]*(len(obstacleGrid[0])-1)

        for row in obstacleGrid:
            dp2 = []
            for obstacle,above in zip(row,dp): dp2.append(0 if obstacle else (above + (dp2[-1] if dp2 else 0)))
            dp = dp2

        return dp[-1]

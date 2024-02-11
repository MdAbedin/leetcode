class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        R,C = len(grid),len(grid[0])
        dp = [[-inf]*C for c in range(C)]
        dp[0][-1] = grid[0][0]+grid[0][-1]

        for r in range(1,R):
            dp2 = [[-inf]*C for c in range(C)]
            
            for i1 in range(C):
                for i2 in range(C):
                    for i3 in range(i1-1,i1+2):
                        for i4 in range(i2-1,i2+2):
                            if i3 not in range(C) or i4 not in range(C): continue

                            if i3 == i4: dp2[i3][i4] = max(dp2[i3][i4],dp[i1][i2]+grid[r][i3])
                            else: dp2[i3][i4] = max(dp2[i3][i4],dp[i1][i2]+grid[r][i3]+grid[r][i4])

            dp = dp2

        return max(map(max,dp))

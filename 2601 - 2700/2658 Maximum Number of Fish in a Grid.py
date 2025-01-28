class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        R,C = len(grid),len(grid[0])
        ans = 0
        
        for r,c in product(range(R),range(C)):
            if grid[r][c] == 0: continue
                
            bfs = [[r,c]]
            ans2 = grid[r][c]
            grid[r][c] = 0

            for r2,c2 in bfs:
                for r3,c3 in [[r2+1,c2],[r2-1,c2],[r2,c2+1],[r2,c2-1]]:
                    if r3 not in range(R) or c3 not in range(C) or grid[r3][c3] == 0: continue
                    ans2 += grid[r3][c3]
                    grid[r3][c3] = 0
                    bfs.append([r3,c3])
                        
            ans = max(ans,ans2)
        
        return ans

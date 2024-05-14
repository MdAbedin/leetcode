class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        R,C = len(grid),len(grid[0])
        dfs = [[r,c,grid[r][c],{(r,c)}] for r in range(R) for c in range(C) if grid[r][c] != 0]
        ans = 0

        while dfs:
            r,c,g,seen = dfs.pop()
            ans = max(ans,g)

            for r2,c2 in [[r+1,c],[r-1,c],[r,c+1],[r,c-1]]:
                if r2 not in range(R) or c2 not in range(C) or grid[r2][c2] == 0 or (r2,c2) in seen: continue
                dfs.append([r2,c2,g+grid[r2][c2],seen|{(r2,c2)}])

        return ans

class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        R,C = len(grid),len(grid[0])
        MOD = 10**9+7
        ans = [[0]*C for i in range(R)]

        for val,r,c in sorted([grid[r][c],r,c] for r in range(R) for c in range(C)):
            ans[r][c] += 1

            for r2,c2 in [[r+1,c],[r-1,c],[r,c+1],[r,c-1]]:
                if r2 in range(R) and c2 in range(C) and grid[r2][c2] < val: ans[r][c] += ans[r2][c2]

            ans[r][c] %= MOD

        return sum(map(sum,ans))%MOD

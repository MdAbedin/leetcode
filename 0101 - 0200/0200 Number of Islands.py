class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R,C = len(grid),len(grid[0])
        ans = 0

        for r in range(R):
            for c in range(C):
                if grid[r][c] != "1": continue

                ans += 1
                bfs = [(r,c)]

                for r2,c2 in bfs:
                    for r3,c3 in [[r2+1,c2],[r2-1,c2],[r2,c2+1],[r2,c2-1]]:
                        if r3 not in range(R) or c3 not in range(C) or grid[r3][c3] != "1": continue
                        grid[r3][c3] = "2"
                        bfs.append((r3,c3))

        return ans

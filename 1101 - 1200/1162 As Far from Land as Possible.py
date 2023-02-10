class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        R,C = len(grid),len(grid[0])
        land_cells = [deque(c for c in range(C) if row[c] == 1) for row in grid]
        ans = -1

        for c in range(C):
            for r in range(R):
                if grid[r][c] == 0:
                    cur_ans = inf

                    for r2,row_land_cells in enumerate(land_cells):
                        if len(row_land_cells) >= 2 and abs(c - row_land_cells[1]) <= abs(c - row_land_cells[0]): row_land_cells.popleft()
                        if row_land_cells: cur_ans = min(cur_ans, abs(r-r2) + abs(c - row_land_cells[0]))
                        
                    if cur_ans != inf: ans = max(ans, cur_ans)

        return ans

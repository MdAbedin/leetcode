class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        grid = [[1]*col for r in range(row)]
        possible = set()

        for i in range(len(cells)-1,-1,-1):
            r0,c0 = cells[i]
            r0 -= 1
            c0 -= 1
            grid[r0][c0] = 0

            if r0 == row-1 or any(r2 in range(row) and c2 in range(col) and (r2,c2) in possible for r2,c2 in [[r0+1,c0],[r0-1,c0],[r0,c0+1],[r0,c0-1]]):
                possible.add((r0,c0))
                dfs = [[r0,c0]]

                while dfs:
                    r,c = dfs.pop()
                    if r == 0: return i

                    for r2,c2 in [[r+1,c],[r-1,c],[r,c+1],[r,c-1]]:
                        if r2 in range(row) and c2 in range(col) and grid[r2][c2] == 0 and (r2,c2) not in possible:
                            possible.add((r2,c2))
                            dfs.append([r2,c2])

class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        start = [[r,c] for r in range(R) for c in range(C) if grid[r][c] == "*"][0]
        
        bfs = deque([tuple(start)])
        seen = {tuple(start)}
        moves = 0

        while bfs:
            for i in range(len(bfs)):
                r, c = bfs.popleft()
                if grid[r][c] == "#": return moves

                for nr, nc in [[r+1,c],[r-1,c],[r,c+1],[r,c-1]]:
                    if nr in range(R) and nc in range(C) and (nr,nc) not in seen and grid[nr][nc] != "X":
                        bfs.append((nr,nc))
                        seen.add((nr,nc))

            moves += 1

        return -1

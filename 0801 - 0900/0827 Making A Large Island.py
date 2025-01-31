class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        R,C = len(grid),len(grid[0])
        sizes = {0:0}
        seen = set()
        ID = 1

        for r,c in product(range(R),range(C)):
            if grid[r][c] == 0 or (r,c) in seen: continue

            seen.add((r,c))
            bfs = [[r,c]]

            for r2,c2 in bfs:
                for r3,c3 in [[r2+1,c2],[r2-1,c2],[r2,c2+1],[r2,c2-1]]:
                    if r3 not in range(R) or c3 not in range(C) or grid[r3][c3] == 0 or (r3,c3) in seen: continue
                    seen.add((r3,c3))
                    bfs.append([r3,c3])

            for r2,c2 in bfs: grid[r2][c2] = ID
            sizes[ID] = len(bfs)
            ID += 1

        return max(max(sizes.values(),default=0),max((grid[r][c]==0)+sum(map(sizes.get,{grid[r2][c2] for r2,c2 in [[r+1,c],[r-1,c],[r,c+1],[r,c-1]] if r2 in range(R) and c2 in range(C)})) for r,c in product(range(R),range(C))))

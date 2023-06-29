class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        R,C = len(grid),len(grid[0])
        r0,c0 = [[r,c] for r,c in product(range(R),range(C)) if grid[r][c] == "@"][0]
        key_count = sum(c.islower() for row in grid for c in row)

        bfs = deque([[r0,c0,[False]*key_count,0]])
        seen = {(r0,c0,tuple([False]*key_count))}

        while bfs:
            r,c,keys,moves = bfs.popleft()

            if all(keys): return moves

            for r2,c2 in [[r+1,c],[r-1,c],[r,c+1],[r,c-1]]:
                if r2 in range(R) and c2 in range(C) and grid[r2][c2] != "#" and not(grid[r2][c2].isupper() and not keys[ord(grid[r2][c2])-ord("A")]):
                    keys2 = keys[:]
                    if grid[r2][c2].islower(): keys2[ord(grid[r2][c2])-ord("a")] = True
                    
                    if (r2,c2,tuple(keys2)) not in seen:
                        seen.add((r2,c2,tuple(keys2)))
                        bfs.append([r2,c2,keys2,moves+1])

        return -1

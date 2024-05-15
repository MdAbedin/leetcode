class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        N = len(grid)
        bfs = [[r,c,0] for r,c in product(range(N),repeat=2) if grid[r][c] == 1]
        dists = [[0 if grid[r][c] == 1 else -1 for c in range(N)] for r in range(N)]

        for r,c,d in bfs:
            for r2,c2 in [[r+1,c],[r-1,c],[r,c+1],[r,c-1]]:
                if r2 not in range(N) or c2 not in range(N) or dists[r2][c2] != -1: continue
                dists[r2][c2] = d+1
                bfs.append([r2,c2,d+1])

        ans = [[-inf]*N for _ in range(N)]
        ans[0][0] = dists[0][0]
        pq = [[-dists[0][0],0,0]]

        while pq:
            s,r,c = heappop(pq)
            
            for r2,c2 in [[r+1,c],[r-1,c],[r,c+1],[r,c-1]]:
                if r2 not in range(N) or c2 not in range(N) or (s2 := min(-s,dists[r2][c2])) <= ans[r2][c2]: continue
                ans[r2][c2] = s2
                heappush(pq,[-s2,r2,c2])

        return ans[-1][-1]

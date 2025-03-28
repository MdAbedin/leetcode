class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        R,C = len(grid),len(grid[0])
        pq = [[grid[0][0],0,0]]
        ans = {}
        points = 0

        for m in range(1,10**6+1):
            while pq and pq[0][0] < m:
                r,c = heappop(pq)[1:]
                grid[r][c] = None
                points += 1

                for r2,c2 in [[r+1,c],[r-1,c],[r,c+1],[r,c-1]]:
                    if r2 not in range(R) or c2 not in range(C) or grid[r2][c2] == None: continue

                    heappush(pq,[grid[r2][c2],r2,c2])
                    grid[r2][c2] = None

            ans[m] = points

        return list(map(ans.get,queries))

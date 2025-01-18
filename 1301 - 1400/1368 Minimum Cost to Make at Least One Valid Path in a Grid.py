class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        R,C = len(grid),len(grid[0])
        pq = [[0,0,0]]
        costs = defaultdict(lambda:inf,{(0,0):0})
        dirs = {
            1:[0,1],
            2:[0,-1],
            3:[1,0],
            4:[-1,0],
        }

        while pq:
            cost,r,c = heappop(pq)
            if cost > costs[r,c]: continue

            for dir_id,(dr,dc) in dirs.items():
                cost2 = cost + (0 if dir_id == grid[r][c] else 1)
                r2,c2 = r+dr,c+dc

                if r2 not in range(R) or c2 not in range(C) or cost2 >= costs[r2,c2]: continue

                costs[r2,c2] = cost2
                heappush(pq,[cost2,r2,c2])

        return costs[R-1,C-1]





















class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        R,C = len(heights),len(heights[0])
        pq = [[0,0,0]]
        bests = defaultdict(lambda: inf)
        
        while pq:
            effort,r,c = heappop(pq)
            if effort > bests[r,c]: continue
            if (r,c) == (R-1,C-1): return effort
            
            for r2,c2 in [[r+1,c],[r-1,c],[r,c+1],[r,c-1]]:
                if r2 in range(R) and c2 in range(C):
                    effort2 = max(effort, abs(heights[r][c] - heights[r2][c2]))
                    if effort2 < bests[r2,c2]:
                        bests[r2,c2] = effort2
                        heappush(pq, [effort2,r2,c2])

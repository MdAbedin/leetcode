class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        qs2 = [[] for _ in range(len(heights))]
        for i,(a,b) in enumerate(queries): qs2[max(a,b)].append([i,a,b])
            
        pq = []
        ans = [-1]*len(queries)
        
        for i,h in enumerate(heights):
            for i2,a,b in qs2[i]:
                if a == b or heights[i] > heights[min(a,b)]: ans[i2] = i
                else: heappush(pq,[heights[min(a,b)],i2])

            while pq and pq[0][0] < heights[i]: ans[heappop(pq)[1]] = i
                
        return ans

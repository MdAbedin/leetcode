class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        pq = []
        s = 0
        ans = inf

        for w,q in sorted(zip(wage,quality),key=lambda p: truediv(*p)):
            if len(pq) >= k-1: ans = min(ans,w*(1+s/q))
            heappush(pq,-q)
            s += q
            if len(pq) > k-1: s += heappop(pq)

        return ans

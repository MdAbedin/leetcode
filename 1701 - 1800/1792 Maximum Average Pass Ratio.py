class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        pq = sorted([-((p+1)/(t+1) - p/t),p,t] for p,t in classes)

        for _ in range(extraStudents):
            _,p,t = heappop(pq)
            heappush(pq,[-((p+2)/(t+2) - (p+1)/(t+1)),p+1,t+1])

        return sum(p/t for _,p,t in pq) / len(pq)

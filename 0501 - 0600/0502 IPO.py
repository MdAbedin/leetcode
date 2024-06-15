class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(map(neg,profits),capital),key=lambda p: -p[1])
        pq = []
        
        for i in range(k):
            while projects and projects[-1][1] <= w: heappush(pq, projects.pop())
            if pq: w += -heappop(pq)[0]
        
        return w

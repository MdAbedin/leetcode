class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = deque(sorted([[c,p] for p,c in zip(profits,capital)]))
        pq = []
        capital = w
        
        for i in range(k):
            while projects and projects[0][0] <= capital:
                c,p = projects.popleft()
                heappush(pq, [-p,c])
                
            if pq: capital += -heappop(pq)[0]
        
        return capital

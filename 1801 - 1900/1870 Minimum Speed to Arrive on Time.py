class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def works(speed): return sum(d//speed + (1 if d%speed != 0 else 0) for d in dist[:-1]) + dist[-1]/speed <= hour
        
        ans = bisect_left(range(1,10**7+1),True,key=works)+1

        return -1 if ans == 10**7+1 else ans

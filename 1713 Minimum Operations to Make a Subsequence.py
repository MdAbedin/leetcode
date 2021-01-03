class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        ts = set(target)
        na = []
        for a in arr:
            if a in ts: na.append(a)
                
        locs = {target[i]:i for i in range(len(target))}
        na = [locs[v] for v in na]
        
        ans = 0
        d = [inf]*(len(na)+1)
        d[0]=-inf
        
        for i in range(len(na)):
            j = bisect_left(d, na[i])
            if d[j-1] < na[i] < d[j]:
                d[j] = na[i]
                
        return len(target)-max(i for i in range(len(d)) if d[i]<inf)

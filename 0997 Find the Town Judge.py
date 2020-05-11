class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        trust_counts = defaultdict(lambda: [0,0])
        
        for truster, trusted in trust:
            trust_counts[truster][0] += 1
            trust_counts[trusted][1] += 1
            
        candidates = set()
        
        for i in range(1,N+1):
            if trust_counts[i][0] == 0 and trust_counts[i][1] == N-1:
                candidates.add(i)
                
        return next(iter(candidates)) if len(candidates) == 1 else -1

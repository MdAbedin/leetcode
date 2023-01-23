class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_counts = defaultdict(lambda: [0,0])
        
        for truster, trusted in trust:
            trust_counts[truster][0] += 1
            trust_counts[trusted][1] += 1
            
        candidates = [person for person in range(1,n+1) if trust_counts[person] == [0,n-1]]
        
        return candidates[0] if len(candidates) == 1 else -1

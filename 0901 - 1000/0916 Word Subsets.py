class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        counts = Counter()
        
        for w in words2:
            for c,count in Counter(w).items():
                counts[c] = max(counts[c],count)

        return [w for w in words1 if Counter(w) >= counts]

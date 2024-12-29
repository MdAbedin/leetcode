class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        m = 10**9+7
        counts = list(map(Counter,zip(*words)))
        
        @cache
        def solve(i,k):
            if i == len(target): return 1
            if k >= len(words[0]): return 0
            return (counts[k][target[i]]*solve(i+1,k+1)+solve(i,k+1))%m
            
        return solve(0,0)

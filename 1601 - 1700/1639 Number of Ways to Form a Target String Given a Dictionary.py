class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9+7
        counters = [Counter(col) for col in zip(*words)]
        
        @cache
        def solve(i,k):
            if len(target)-i > len(words[0])-k: return 0
            if i == len(target): return 1
            return ((counters[k][target[i]] * solve(i+1,k+1))%MOD + solve(i,k+1))%MOD
            
        return solve(0,0)

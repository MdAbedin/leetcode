class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        @cache
        def solve(i):
            if i >= len(stoneValue): return 0,0

            best = -inf,-inf

            for take in range(1,4):
                scores = solve(i+take)
                scores = sum(stoneValue[i:i+take])+scores[1],scores[0]
                best = max(best,scores)

            return best

        a,b = solve(0)
        
        return "Alice" if a > b else ("Bob" if b > a else "Tie")

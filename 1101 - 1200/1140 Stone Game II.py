class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        @cache
        def solve(i,M):
            if i >= len(piles): return 0,0

            ans = (0,0)

            for x in range(1,2*M+1):
                s0,s1 = solve(i+x,max(M,x))
                ans = max(ans,(sum(piles[i:i+x])+s1,s0))

            return ans

        return solve(0,1)[0]

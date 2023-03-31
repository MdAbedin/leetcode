class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        R,C = len(pizza),len(pizza[0])
        MOD = 10**9+7

        @cache
        def solve(r,c,pieces):
            if pieces == 1: return 1 if any(pizza[r2][c2] == "A" for r2 in range(r,R) for c2 in range(c,C)) else 0

            ans = 0
            apple_found = False

            for cut_r in range(r,R-1):
                if apple_found or any(pizza[cut_r][c2] == "A" for c2 in range(c,C)):
                    apple_found = True
                    ans += solve(cut_r+1,c,pieces-1)
                    ans %= MOD

            apple_found = False

            for cut_c in range(c,C-1):
                if apple_found or any(pizza[r2][cut_c] == "A" for r2 in range(r,R)):
                    apple_found = True
                    ans += solve(r,cut_c+1,pieces-1)
                    ans %= MOD

            return ans

        return solve(0,0,k)

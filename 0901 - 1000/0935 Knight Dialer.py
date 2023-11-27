MOD = 10**9+7
ans = [0,10,20,46,104,240,544]

class Solution:
    @cache
    def knightDialer(self, n: int) -> int:
        return ans[n] if n < len(ans) else (6*self.knightDialer(n-2)-4*self.knightDialer(n-4))%MOD

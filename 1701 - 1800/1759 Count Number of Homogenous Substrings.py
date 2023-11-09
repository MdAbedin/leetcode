class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 10**9+7
        ans = 0
        streak = 0
        prev = None

        for c in s:
            if c == prev: streak += 1
            else: streak = 1
            ans += streak
            ans %= MOD
            prev = c

        return ans

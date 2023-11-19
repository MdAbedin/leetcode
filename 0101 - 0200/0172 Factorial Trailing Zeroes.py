class Solution:
    def trailingZeroes(self, n: int) -> int:
        m = 5
        ans = 0

        while m <= n:
            ans += n//m
            m *= 5
        
        return ans

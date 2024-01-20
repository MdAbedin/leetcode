class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9+7
        ans = 0
        add = 0
        s = []

        for num in arr:
            c = 1

            while s and s[-1][0] >= num:
                add -= prod(s[-1])
                c += s.pop()[1]

            s.append((num,c))
            add += prod(s[-1])
            ans += add
            ans %= MOD

        return ans

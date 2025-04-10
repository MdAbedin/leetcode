class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        def solve(x):
            x = str(x)
            ans = 0

            for i in range(len(x)-len(s)):
                ans += min(limit+1,int(x[i])) * (limit+1)**(len(x)-len(s)-i-1)
                if int(x[i]) > limit: break
            else:
                ans += (int(x[:-len(s)]+s) <= int(x))

            return ans

        return solve(finish)-solve(start-1)

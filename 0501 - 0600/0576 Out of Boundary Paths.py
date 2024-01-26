class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9+7
        dp = [[0]*(n+2) for i in range(m+2)]
        dp[startRow+1][startColumn+1] = 1

        for i in range(maxMove):
            dp2 = [[0]*(n+2) for i2 in range(m+2)]

            for r in range(m+2):
                for c in range(n+2):
                    if r in [0,m+1] or c in [0,n+1]:
                        dp2[r][c] += dp[r][c]
                    else:
                        for r2,c2 in [[r+1,c],[r-1,c],[r,c+1],[r,c-1]]:
                            dp2[r2][c2] += dp[r][c]
                            dp2[r2][c2] %= MOD

            dp = dp2

        return sum(dp[r][c] for r in range(m+2) for c in range(n+2) if r in [0,m+1] or c in [0,n+1])%MOD

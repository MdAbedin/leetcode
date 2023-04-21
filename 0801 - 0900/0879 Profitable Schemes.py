class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10**9+7
        dp = defaultdict(int,{(0,0):1})

        for g,p in zip(group,profit):
            dp2 = dp.copy()

            for (g2,p2),ways in dp.items():
                if g2+g <= n:
                    dp2[g2+g,min(minProfit,p2+p)] += ways
                    dp2[g2+g,min(minProfit,p2+p)] %= MOD

            dp = dp2

        return sum(dp[g,minProfit] for g in range(n+1)) % MOD

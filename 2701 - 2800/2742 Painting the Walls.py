class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        dp = [0]+[sum(cost)]*len(cost)

        for c,t in zip(cost,time):
            dp2 = dp[:]
            for t2 in range(len(dp2)): dp2[t2] = min(dp2[t2],dp[max(0,t2-t-1)]+c)
            dp = dp2

        return dp[-1]

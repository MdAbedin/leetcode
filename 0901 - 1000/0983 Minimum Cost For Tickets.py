class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = {}

        for day in range(1,366):
            dp[day] = min(dp.get(day-1,0) + costs[0], dp.get(day-7,0) + costs[1], dp.get(day-30,0) + costs[2]) if day in days else dp.get(day-1,0)

        return dp[365]

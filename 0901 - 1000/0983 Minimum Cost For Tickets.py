class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @cache
        def solve(i): return 0 if i == len(days) else min(c+solve(bisect_left(days,days[i]+d)) for d,c in zip([1,7,30],costs))
        return solve(0)

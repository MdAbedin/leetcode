class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10**9+7

        @cache
        def solve(i,f):
            if f < 0: return 0
            return ((i == finish) + sum(solve(i2,f-abs(locations[i]-locations[i2])) for i2 in range(len(locations)) if i2 != i))%MOD

        return solve(start,fuel)

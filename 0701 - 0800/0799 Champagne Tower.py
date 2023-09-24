class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        @cache
        def solve(r,c):
            if c not in range(r+1): return 0
            if (r,c) == (0,0): return poured
            return max(solve(r-1,c)-1,0)/2 + max(solve(r-1,c-1)-1,0)/2

        return min(1,solve(query_row,query_glass))

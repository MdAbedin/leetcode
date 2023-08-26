class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        @cache
        def solve(r,i):
            if r == len(triangle): return 0
            if i == len(triangle[r]): return inf
            return triangle[r][i] + min(solve(r+1,i),solve(r+1,i+1))

        return solve(0,0)

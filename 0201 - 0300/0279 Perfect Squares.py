class Solution:
    def numSquares(self, n: int) -> int:
        squares = [x**2 for x in range(1,int(sqrt(n))+1)]

        @cache
        def solve(x): return 0 if x == 0 else min([1+solve(x-s) for s in squares if s <= x],default=inf)

        return solve(n)

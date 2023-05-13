class Solution:

    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:

        MOD = 10**9+7

        

        @cache

        def solve(length):

            if length < 0: return 0

            if length == 0: return 1

            

            return (solve(length-zero)+solve(length-one))%MOD

        

        return sum(solve(length) for length in range(low,high+1))%MOD

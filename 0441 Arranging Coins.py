class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((-1 + sqrt(1 - 4*-2*n))/2)

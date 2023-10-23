class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and log(n,4) == int(log(n,4))

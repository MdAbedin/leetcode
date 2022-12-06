class Solution:
    def findNthDigit(self, n: int) -> int:
        subtract = 0
        i = 0

        while subtract + (i+1) * 9*10**i < n:
            subtract += (i+1) * 9*10**i
            i += 1
        
        skip, digit = divmod(n - subtract - 1, i + 1)

        return int(str(10**i + skip)[digit])

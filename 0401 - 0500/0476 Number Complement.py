class Solution:
    def findComplement(self, num: int) -> int:
        ans = 0
        i = 0
        while num:
            bit = num%2
            ans += 2**i * (1-bit)
            num >>= 1
            i += 1
            
        return ans

class Solution:
    def reverseBits(self, n: int) -> int:
        bstring = bin(n)[2:]
        bstring = '0'*(32-len(bstring))+bstring
        bstring = bstring[::-1]
        return int(bstring, base=2)

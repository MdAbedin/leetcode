class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        c = s.count("1")
        ans = 2**len(s) - 2**(len(s)-c+1) + 1
        return bin(ans)[2:].zfill(len(s))

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        bstr = bin(num)[2:]
        bstr = "0"*(32-len(bstr))+bstr
        
        return num > 0 and bstr.count("1") == 1 and (31-bstr.index("1"))%2 == 0

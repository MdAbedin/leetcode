class Solution:
    def toHex(self, num: int) -> str:
        if num == 0: return "0"
        
        num = (num+2**32)%(2**32)
        ans = []

        while num:
            ans.append(hexdigits[num%16])
            num //= 16

        return "".join(ans[::-1])

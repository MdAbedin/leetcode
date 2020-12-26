class Solution:
    def maximumBinaryString(self, b: str) -> str:
        ans = ""
        for i in range(len(b)):
            c = b[i]
            if c == "0":
                b = b[i:]
                break
            ans += c
            
            if i == len(b)-1:
                b = ""
            
        ans += (b.count("0")-1)*"1" + ("0" if "0" in b else "") + "1"*(b.count("1"))
        return ans

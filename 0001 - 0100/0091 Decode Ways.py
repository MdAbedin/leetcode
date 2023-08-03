class Solution:
    def numDecodings(self, s: str) -> int:
        cur,prev = 1,0
        
        for i in range(len(s)): cur,prev = (cur if int(s[i]) in range(1,10) else 0) + (prev if i-1 >= 0 and s[i-1] != "0" and int(s[i-1:i+1]) in range(1,27) else 0),cur

        return cur

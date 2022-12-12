class Solution:
    def countLetters(self, S: str) -> int:
        ans = 1
        cur = 1
        
        for i in range(1,len(S)):
            if S[i] != S[i-1]: cur = 0
            cur += 1
            ans += cur
            
        return ans

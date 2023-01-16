class Solution:
    def longestPalindrome(self, s: str) -> str:
        s = "_".join(list(s))
        ans = ""
        
        for i in range(len(s)):
            for dist in range(len(s)+1):
                if any(j not in range(len(s)) for j in (i-dist,i+dist)) or s[i-dist] != s[i+dist]: break
                    
            cur_ans = s[i-dist+1 : i+dist].replace("_", "")
            
            if len(cur_ans) > len(ans): ans = cur_ans
        
        return ans

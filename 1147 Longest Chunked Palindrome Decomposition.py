class Solution:
    def longestDecomposition(self, text: str) -> int:
        ans = 0
        l,r = 0,len(text)-1
        
        while l <= r:
            i = 0
            
            while text[l:l+i+1] != text[r-i:r+1]:
                i += 1
                
            ans += 1 if i == r-l else 2
            l,r = l+i+1, r-i-1
            
        return ans

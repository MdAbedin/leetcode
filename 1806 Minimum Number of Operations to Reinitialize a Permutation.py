class Solution:
    def reinitializePermutation(self, n: int) -> int:
        if n == 2: return 1
        
        i = 2
        ans = 1
        
        while i != 1:
            if i >= n/2:
                i = (i-n//2)*2+1
            else:
                i = i*2
                
            ans += 1
            
        return ans

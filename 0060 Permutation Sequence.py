class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorials = [1]*n
        for i in range(1,len(factorials)): factorials[i] = (i+1)*factorials[i-1]
        
        ans = ''
        digits = [str(i) for i in range(1, n+1)]
        k -= 1
        
        for i in range(n-1):
            group = k//factorials[-1*i-2]
            ans += digits[group]
            del digits[group]
            k = k%factorials[-1*i-2]
            
        return ans+digits[0]

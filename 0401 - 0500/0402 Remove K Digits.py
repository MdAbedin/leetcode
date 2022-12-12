class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        num = str(num)
        
        if len(num) <= k:
            return '0'
        
        l = 0
        ans = ''
        k2 = k
        
        while k:
            found = False
            
            for i in range(10):
                for j in range(l,min(l+k+1,len(num))):
                    if num[j] == str(i):
                        ans += str(num[j])
                        
                        if len(ans) == len(num)-k2:
                            return str(int(ans))
                        
                        k -= j-l
                        l = j+1
                        found = True
                        break
                        
                if found:
                    break
                    
        ans += num[l:]
        return str(int(ans))

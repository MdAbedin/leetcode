class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        ans = 0
        i = 0
        
        while n//(2**i):
            ans += 2**i if ((m//(2**i))%2 and m//(2**i) == n//(2**i)) else 0
            i += 1
            
        return ans

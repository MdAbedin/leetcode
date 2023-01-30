class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1: return n
        cur,prev,prev2 = 1,1,0
        
        for i in range(3,n+1):
            cur,prev,prev2 = cur+prev+prev2,cur,prev
        
        return cur

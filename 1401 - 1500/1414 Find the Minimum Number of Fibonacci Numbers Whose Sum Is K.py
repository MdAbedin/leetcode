class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        if k <= 1:
            return k
        
        a,b = 1,1
        
        while b <= k:
            b = a+b
            a = b-a
            
        return 1 + self.findMinFibonacciNumbers(k-a)

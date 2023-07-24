class Solution:
    @cache
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        if n < 0: return 1/self.myPow(x,-n)
        return self.myPow(x,n//2)*self.myPow(x,n//2)*(x if n%2 == 1 else 1)

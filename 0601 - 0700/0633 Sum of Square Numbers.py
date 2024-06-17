class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        return any(round(sqrt(c-x**2))**2 == c-x**2 for x in range(int(sqrt(c))+1))

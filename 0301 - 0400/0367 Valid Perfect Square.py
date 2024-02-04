class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return (bisect_left(range(num+1),num,key=lambda x: x**2))**2 == num

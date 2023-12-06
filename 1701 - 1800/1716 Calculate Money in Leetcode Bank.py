class Solution:
    def totalMoney(self, n: int) -> int:
        return 28*(n//7) + 7*(n//7*(n//7-1))//2 + ((n//7+1)*2+(n-1)%7)*(n%7)//2

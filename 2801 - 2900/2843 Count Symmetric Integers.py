class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        return sum(sum(map(int,s[:len(s)//2])) == sum(map(int,s[len(s)//2:])) for num in range(low,high+1) if len(s:=str(num))%2 == 0)

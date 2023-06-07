class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        a,b,c = map(lambda x: list(map(int,f"{x:b}".zfill(30))),[a,b,c])
        return sum(1 if b3 == 1 else b1+b2 for b1,b2,b3 in zip(a,b,c) if b1|b2 != b3)

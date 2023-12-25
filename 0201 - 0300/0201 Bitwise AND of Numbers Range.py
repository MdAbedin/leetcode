class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        return sum(2**i for i in range(31) if left//(2**i) == right//(2**i) and left//(2**i)%2 == 1)

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        inds = [i for i in range(31,-1,-1) if num1&(1<<i)] + [i for i in range(32) if not num1&(1<<i)]
        return sum(1<<i for i in inds[:num2.bit_count()])

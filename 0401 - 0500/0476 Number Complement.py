class Solution:
    def findComplement(self, num: int) -> int:
        return sum(0 if num&(1<<i) else 1<<i for i in range(num.bit_length()))

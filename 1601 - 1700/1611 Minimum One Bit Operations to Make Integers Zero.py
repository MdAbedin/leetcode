class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        return 0 if n == 0 else 2**n.bit_length()-1-self.minimumOneBitOperations(n-2**(n.bit_length()-1))

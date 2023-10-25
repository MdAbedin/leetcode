class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        return 0 if n == 1 else (self.kthGrammar(n-1,k) if k <= 2**(n-2) else 1-self.kthGrammar(n-1,k-2**(n-2)))

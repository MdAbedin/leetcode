class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1: return 0
        
        return self.kthGrammar(N-1, K) if K <= 2**(N-2) else 1-self.kthGrammar(N-1,K-2**(N-2))

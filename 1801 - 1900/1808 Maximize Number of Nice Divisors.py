class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        MOD = int(1e9+7)
        
        if primeFactors < 4:
            return primeFactors
        
        if primeFactors % 3 == 0:
            return pow(3,primeFactors//3,MOD)
        elif primeFactors % 3 == 1:
            return (pow(3,primeFactors//3-1,MOD)*4)%MOD
        else:
            return (pow(3,primeFactors//3,MOD)*2)%MOD

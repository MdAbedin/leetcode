class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        MOD = int(1e9+7)
        if max(a,b)%min(a,b) == 0: return (min(a,b)*n) % MOD
        ans = 0
        gcd_ab = gcd(a,b)
        
        for i in range(n//(a//gcd_ab + b//gcd_ab - 1)):
            ans = (ans + (a*b)//gcd_ab) % MOD
            
        new_a,new_b = 0,0
        
        for i in range(n % (a//gcd_ab + b//gcd_ab - 1)):
            if new_a+a < new_b+b:
                new_a += a
            else:
                new_b += b
            
        return (ans + max(new_a, new_b)) % MOD

class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        twos = [2**i for i in range(23)]
        countsd = Counter(deliciousness)
        counts = sorted(Counter(deliciousness).items())
        ans = 0
        MOD = int(1e9+7)
        
        for two in twos:
            for v,c in counts:
                if v > two//2: break
                if v == two-v:
                    ans += (countsd[two-v]*(countsd[two-v]-1))//2 if two-v in countsd else 0
                else:
                    ans += countsd[v]*countsd[two-v] if two-v in countsd else 0
                ans = ans % MOD
                    
        return ans

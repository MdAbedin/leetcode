class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        sums = [0]*(int(5*1e4))
        sums2 = [0]*(int(5*1e4))
        
        for i in range(len(apples)):
            sums[i] += apples[i]
            sums[i+days[i]] += -1*apples[i]
            sums2[i+days[i]] += -1*apples[i]

        ans = 0
        sub = 0
        
        for i in range(len(sums)):
            sums[i] += sums[i-1] if i-1>=0 else 0
            sub = max(0,sub+sums2[i])
            
            if sums[i]-sub > 0:
                ans += 1
                sub += 1
        
        return ans

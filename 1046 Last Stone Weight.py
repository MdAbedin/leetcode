class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        counts = [0]*1001
        for weight in stones:
                counts[weight] += 1
            
        while True:
            found = 0
            max1 = -1
            max2 = -1
            i = 1000
            
            while i:
                if counts[i]:
                    found += 1
                    counts[i] -= 1
                    
                    if found == 1:
                        max1 = i
                    else:
                        max2 = i
                    
                if found == 2:
                    break
                
                if counts[i]:
                    i += 1
                    
                i -= 1
                
            if found == 2:
                if max1 != max2:
                    counts[max1-max2] += 1
            else:
                return max1 if found == 1 else 0

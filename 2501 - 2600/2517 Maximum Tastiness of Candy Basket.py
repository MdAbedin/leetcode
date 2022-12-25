class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        
        def fails(t):
            prev = price[0]
            found = 1
            
            for i in range(1,len(price)):
                if price[i] >= prev+t:
                    prev = price[i]
                    found += 1
            
            return found < k
        
        return bisect_left(range(price[-1]-price[0]+1), True, key = fails)-1

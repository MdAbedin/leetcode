class Solution:

    def __init__(self, w: List[int]):
        self.total = sum(w)
        
        for i in range(1, len(w)):
            w[i] += w[i-1]
            
        self.w = w
        
    def pickIndex(self) -> int:
        ans = 0
        stop = randrange(self.total)
        
        l,r = 0, len(self.w)-1
        while l <= r:
            mid = (l+r)//2
            
            if self.w[mid] > stop:
                ans = mid
                r = mid-1
            else:
                l = mid+1
                
        return ans

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

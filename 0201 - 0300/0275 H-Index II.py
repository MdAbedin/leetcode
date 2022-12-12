class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l, r = 1, len(citations)
        ans = 0
        
        while l <= r:
            mid = (l+r)//2
            
            if citations[-1*mid] >= mid:
                ans = mid
                l = mid+1
            else:
                r = mid-1
                
        return ans

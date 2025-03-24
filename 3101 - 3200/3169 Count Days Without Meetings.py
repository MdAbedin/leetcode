class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        ans = 0
        p = 0
        
        for s,e in sorted(meetings):
            ans += max(0,s-p-1)
            p = max(p,e)
            
        return ans+max(0,days-p)

class Solution:
    def findScore(self, nums: List[int]) -> int:
        pq = [[num,i] for i,num in enumerate(nums)]
        heapify(pq)
        used = set()
        ans = 0
        
        while True:
            while pq and pq[0][1] in used: heappop(pq)
            if not pq: break
            
            num,i = heappop(pq)
            ans += num
            used |= {i-1,i,i+1}
        
        return ans

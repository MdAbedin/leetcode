class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        pq = [[-1*nums[0], 0]]
        
        for i in range(1,len(nums)):
            while pq[0][1] < i-k:
                heappop(pq)
                
            if i == len(nums)-1:
                return pq[0][0]*-1 + nums[i]
            
            heappush(pq, [-1*(pq[0][0]*-1 + nums[i]), i] )
            
        return nums[0]

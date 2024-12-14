class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        min_pq,max_pq = [],[]
        r = ans = 0
        
        for l in range(len(nums)):
            while min_pq and min_pq[0][1] < l: heappop(min_pq)
            while max_pq and max_pq[0][1] < l: heappop(max_pq)
                
            while r < len(nums) and max(-max_pq[0][0] if max_pq else -inf,nums[r]) - min(min_pq[0][0] if min_pq else inf,nums[r]) <= 2:
                heappush(min_pq,[nums[r],r])
                heappush(max_pq,[-nums[r],r])
                ans += r+1-l
                r += 1
        
        return ans

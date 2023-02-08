class Solution:
    def jump(self, nums: List[int]) -> int:
        pq = [[-1,0]]

        for i,num in enumerate(nums):
            while pq and pq[0][1] < i: heappop(pq)
            
            jumps = pq[0][0]+1
            if i == len(nums)-1: return jumps
            heappush(pq, [jumps, i+nums[i]])

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        
        def works(diff):
            prev,cur = 0,0
            for i in range(1,len(nums)): prev,cur = cur,max(cur,prev + (nums[i]-nums[i-1] <= diff))
            return cur >= p
        
        return bisect_left(range(10**9+1),True,key = works)

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        ps = nums[0]+nums[1]
        ans = -1
        
        for i in range(2,len(nums)):
            if ps > nums[i]: ans = ps+nums[i]
            ps += nums[i]
            
        return ans

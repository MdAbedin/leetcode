class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
            
        if nums[-1] < s:
            return 0
        
        ans = 0
        for i,num in enumerate(nums):
            if num >= s:
                ans = i+1
                break
                
        for i in range(ans-1,len(nums)):
            j = i-ans+1
            
            while nums[i]-nums[j] >= s:
                ans = i-j
                j += 1
                
        return ans

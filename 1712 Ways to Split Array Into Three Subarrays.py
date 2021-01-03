class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        
        MOD = int(1e9+7)
        ans = 0
        S = sum(nums)
        
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
            
        for i in range(len(nums)):
            l = max(i+1,bisect_left(nums, nums[i]*2))
            if l >= len(nums): break
            if S-nums[l] >= nums[l] - nums[i]:
                r = min(len(nums)-1,bisect_right(nums, (S+nums[i])/2))
                ans += r-l
                ans %= MOD
                
        return ans

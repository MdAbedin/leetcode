class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
      last = {0:-1}
      s = 0
      dp = [0]*len(nums)
      
      for i in range(len(nums)):
        s += nums[i]
        
        if s-target in last:
          dp[i] = max(dp[i-1] if i-1>=0 else 0, 1+ (dp[last[s-target]] if last[s-target]>=0 else 0))
        else:
          dp[i] = dp[i-1] if i-1>=0 else 0
        
        last[s] = i
          
      return dp[-1]

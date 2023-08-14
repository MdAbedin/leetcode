class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        @cache
        def solve(i):
            if i == len(nums): return True
            
            return (i+1 < len(nums) and nums[i] == nums[i+1] and solve(i+2)) or (i+2 < len(nums) and (nums[i] == nums[i+1] == nums[i+2] or nums[i+2] == nums[i]+2 and nums[i+1] == nums[i]+1) and solve(i+3))
        
        return solve(0)

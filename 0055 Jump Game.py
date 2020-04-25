class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthest_index = 0
        i = 0
        
        while i <= furthest_index:
            furthest_index = max(furthest_index, i+nums[i])
            if furthest_index >= len(nums)-1: return True
            i += 1
            
        return False

class Solution:
    def helper(self, l, r):
        if l > r: return 0
        
        shared = self.helper(l+1, r-1)
        
        return max(self.nums[l] + min(self.helper(l+2, r), shared), self.nums[r] + min(shared, self.helper(l, r-2)))
    
    def PredictTheWinner(self, nums: List[int]) -> bool:
        self.nums = nums
        
        return self.helper(0, len(nums)-1) >= min(self.helper(1, len(nums)-1), self.helper(0, len(nums)-2))

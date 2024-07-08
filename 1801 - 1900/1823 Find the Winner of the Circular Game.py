class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums = list(range(1,n+1))
        
        while len(nums) > 1:
            i = (k-1)%len(nums)
            nums = nums[i+1:]+nums[:i]
        
        return nums[0]

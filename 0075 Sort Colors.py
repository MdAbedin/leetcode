class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        reds, whites = 0, 0
        
        for color in nums:
            if color == 0: reds += 1
            if color == 1: whites += 1
                
        for i in range(reds): nums[i] = 0
        for i in range(reds, reds+whites): nums[i] = 1
        for i in range(reds+whites, len(nums)): nums[i] = 2

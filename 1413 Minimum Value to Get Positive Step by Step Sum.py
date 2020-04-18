class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        change = min_change = 0
        
        for num in nums:
            change += num
            min_change = min(min_change, change)
                
        return -1*min_change + 1 if min_change < 0 else 1

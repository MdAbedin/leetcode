class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = {}
        
        for i,num in enumerate(nums):
            if target-num in indexes: return [i, indexes[target-num]]
            indexes[num] = i
